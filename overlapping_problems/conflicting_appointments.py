# Given an array of intervals representing N appointments,
# find out if a person can attend all the appointments.

# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

# Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.


# [1,4], [2,5], [7,9]

# sort the array on the first element
# if arr.start < pre_arr.end
# if start of next is less that previous end, return false, else true

def conflicting_appointments(appointments):

  len_app = len(appointments)

  if len_app < 2:
    return True

  appointments.sort(key=lambda x: x[0])

  for i in range(1, len_app):
    if appointments[i][0] < appointments[i-1][1]:
      return False
  return True


appointments = [[6,7], [2,4], [8,12]]

# print (conflicting_appointments(appointments))


# Given a list of appointments, find all the conflicting appointments.

# Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]

# [[2,3], [3,6], [4,5], [5,7], [7,8]]
# Output:
# [4,5] and [3,6] conflict.
# [3,6] and [5,7] conflict.


# First, sort the appointments on start time
# start = 0, end = 1
# if the arr[0] < prev_arr[1]
# return prev_arr and arr

def if_conflict (arr1, arr2):
  start = 0
  end = 1
  if arr2[start] < arr1[end]:
    print ("{} and {} conflict".format(str(arr1), str(arr2)))


def get_conflict_appointments(apps):
  len_apps = len(apps)

  if len_apps < 2:
    print ("No conflict")

  apps.sort(key= lambda x:x[0])

  for i in range(0, len_apps):
    j = i + 1
    for j in range(j, len_apps):
      if i != j:
        if_conflict(apps[i], apps[j])


apps = [[4,5], [2,3], [3,6], [5,7], [7,8]]
get_conflict_appointments (apps)

