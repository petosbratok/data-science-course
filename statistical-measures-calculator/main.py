import numpy as np

def calculate(arr):

  matrix = np.array(test_case).reshape(3, 3)

  axis_variants = [0, 1, None]
  result = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
  }

  for ax in axis_variants:
    result['mean'].append(matrix.mean(axis=ax))
    result['variance'].append(matrix.var(axis=ax))
    result['standard deviation'].append(matrix.std(axis=ax))
    result['max'].append(matrix.max(axis=ax))
    result['min'].append(matrix.min(axis=ax))
    result['sum'].append(matrix.sum(axis=ax))

  return result
