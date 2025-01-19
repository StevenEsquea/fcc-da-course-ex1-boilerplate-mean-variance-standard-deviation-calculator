import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    new_list = np.array(list)
    new_list = new_list.reshape((3,3))

    calculations = {
        'mean': [new_list.mean(axis=0).tolist(), new_list.mean(axis=1).tolist(), new_list.mean().tolist()],
        'variance': [new_list.var(axis=0).tolist(), new_list.var(axis=1).tolist(), new_list.var().tolist()],
        'standard deviation': [new_list.std(axis=0).tolist(), new_list.std(axis=1).tolist(), new_list.std().tolist()],
        'max': [new_list.max(axis=0).tolist(), new_list.max(axis=1).tolist(), new_list.max().tolist()],
        'min': [new_list.min(axis=0).tolist(), new_list.min(axis=1).tolist(), new_list.min().tolist()],
        'sum': [new_list.sum(axis=0).tolist(), new_list.sum(axis=1).tolist(), new_list.sum().tolist()]
    }
    
    return calculations