import os, sys

##method that removes steps from prerequisites and returns updated list
##plus list of newly available steps
def remove_step_from_prerequisites(step, requirements):
    empties = []
    for requirement in requirements:
        ##if the step we just did is a prerequisite, remove it since it
        ##has been fulfilled
        if step in requirements[requirement]:
            requirements[requirement].remove(step)
            ##if that was the last prerequisite, add the step to the "empty"
            ##list since it no longer has any prerequisites and is "available"
            if len(requirements[requirement]) == 0:
                empties.append(requirement)
    
    ##remove the newly available steps from the requirements
    for empty in empties:
        requirements.pop(empty)
    return requirements, empties



dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

##collect all input, or "requirements"
with open(os.path.join(dirname, "input.txt")) as requirement_list:
    requirements = [requirements.split() for requirements in requirement_list]

prerequisite_set = set()
step_set = set()
requirement_pairs = {}

##store all prerequisite/step pairs and store each in sets to find our starting points
for requirement in requirements:
    prerequisite = requirement[1]
    prerequisite_set.add(prerequisite)
    
    step = requirement[7]
    step_set.add(step)

    if step in requirement_pairs:
        prerequisite_list = list(requirement_pairs[step])
        prerequisite_list.append(prerequisite)
        requirement_pairs[step] = prerequisite_list
    else:
        requirement_pairs[step] = [prerequisite]

##sort alphabetically so the one we choose is at index = 0
available_steps = sorted(prerequisite_set.difference(step_set))
done_steps = []

##loop through all steps and update available steps to find the best next step
while len(available_steps) > 0:
    current_step = available_steps[0]

    prerequisite_list, fresh_steps = remove_step_from_prerequisites(current_step, requirement_pairs)

    ##remove the current step from available_steps since we just "did" it
    available_steps.remove(current_step)

    ##add the newly available steps
    available_steps += fresh_steps

    ##sort again so that the best step is at index = 0
    available_steps = sorted(available_steps)

    ##keep track of steps done
    done_steps.append(current_step)

print("".join(done_steps))