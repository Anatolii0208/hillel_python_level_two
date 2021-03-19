def first_task(a):
    return set(a)==a
def second_task(a,b):
  return [i for i in set(a) if i not in set(b)]
def third_task(a,b):
  c = [i for i in set(b) if i not in a]
  return c