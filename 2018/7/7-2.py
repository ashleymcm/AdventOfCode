import os, sys, string

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

def time_to_complete_task(letter):
    ##return string.ascii_uppercase.index(letter) + 1
    return 60 + 1 + string.ascii_uppercase.index(letter)

##test to see if all workers given are idle
def none_busy(workers):
    for worker in workers:
        if worker.step:
            return False
    
    return True
    
def start_new_step(worker, available_steps):
    worker.step = available_steps[0]
    worker.step_length = time_to_complete_task(worker.step)
    worker.step_progress = 0

    ##remove the current step from available_steps since this worker is
    ##"doing" it
    available_steps.remove(worker.step)
    return worker, available_steps

class Worker:
    def __init__(self):
        self.step = None
        self.step_length = 0
        self.step_progress = 0
    def __repr__(self):
        return "<Worker step:%s step_length:%s step_progress:%s>" % (self.step, self.step_length, self.step_progress)

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

available_steps = sorted(prerequisite_set.difference(step_set))
done_steps = []
second = 0
workers = [Worker(), Worker(), Worker(), Worker(), Worker()]

##loop through all steps and update available steps to find the best next step
while True:
    for worker in workers:
        ##if the worker is idle and there are available steps
        if not worker.step and len(available_steps) > 0:
            worker, available_steps = start_new_step(worker, available_steps)

        ##else if the worker is about to complete a step
        elif worker.step and worker.step_progress == worker.step_length - 1:
            prerequisite_list, fresh_steps = remove_step_from_prerequisites(worker.step, requirement_pairs)
            ##add the newly available steps
            available_steps += fresh_steps
            ##keep track of steps done
            done_steps.append(worker.step)

            ##if there are available steps, start one
            if len(available_steps) > 0:
                worker, available_steps = start_new_step(worker, available_steps)
            ##else just empty worker for next round
            else:
                worker.step = None
                worker.step_length = 0
                worker.step_progress = 0
        ##else if the worker is on a step that is not about to finish
        elif worker.step and worker.step_progress < worker.step_length:
            worker.step_progress += 1
        else:
            ##idle
            continue
    
    ##if no workers have any work, we are done
    if none_busy(workers):
        break

    ##mark that another second has elapsed
    second += 1

print(second)