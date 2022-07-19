# # code goes here
# 2020-01-01 F41.1 2020-01-01
# 2020-01-01 F41.1 2020-01-15
# 2020-02-01 F43.10 2020-01-15
# 2020-02-01 F43.10 2020-02-01
# 2020-02-01 F43.10 2020-02-15
# 2020-04-01 F43.10 2020-02-15
# {'2020-01-01 12:00 PM': 'F41.1', '2020-01-15 12:00 PM': 'F43.10', '2020-02-01 12:00 PM': 'F43.10', '2020-02-15 12:00 PM': 'F43.10'}

# 2020-01-01 F41.1 2020-01-01
# 2020-01-01 F41.1 2020-01-15
# 2020-02-01 F43.10 2020-01-15
# 2020-02-01 F43.10 2020-02-01
# 2020-02-01 F43.10 2020-02-15
# 2020-04-01 F43.10 2020-02-15
# {'2020-01-01 12:00 PM': 'F41.1', '2020-01-15 12:00 PM': 'F43.10', '2020-02-01 12:00 PM': 'F43.10', '2020-02-15 12:00 PM': 'F43.10'}



visits = ["2020-01-01 12:00 PM",
  "2020-01-15 12:00 PM" ,
  "2020-02-01 12:00 PM",
  "2020-02-15 12:00 PM",
]

diagnosis = ["F41.1 - Generalized anxiety disorder noted at 2020-01-01 1:33 PM",
  "F43.10 - Post-traumatic stress disorder, unspecified noted at 2020-02-01 1:22 PM",
  "F43.10 - Post-traumatic stress disorder, unspecified noted at 2020-04-01 1:22 PM"]

def strip_visit_date(visit):
  visit_date = visit.split()
  # print (visit_date[0])
  return visit_date[0]

def strip_diagnosis_date(diagnosis):
  diagnosis_date = diagnosis.split()
  # print(diagnosis_date[-3], diagnosis_date[0])
  return diagnosis_date[-3], diagnosis_date[0]

def map_diagonis(visits, diagnosis):
  visit_counter = 0
  output = {}

  prev_diagnosis_date, prev_diagnosis_code = strip_diagnosis_date(diagnosis[0])
  diagnosis_counter = 1

  while diagnosis_counter < len(diagnosis):
    diagnose = diagnosis[diagnosis_counter]

    curr_diagnosis_date, curr_diagnosis_code = strip_diagnosis_date(diagnose)

    while visit_counter < len(visits):

      visit = visits[visit_counter]
      visit_date = strip_visit_date(visit)

      print (prev_diagnosis_date, prev_diagnosis_code, visit_date)

      if prev_diagnosis_date <= visit_date and  curr_diagnosis_date > visit_date:
        output[visit] = prev_diagnosis_code
      else:
        break

      visit_counter += 1

    prev_diagnosis_code = curr_diagnosis_code
    prev_diagnosis_date = curr_diagnosis_date
    diagnosis_counter += 1


  return output



print (map_diagonis(visits, diagnosis))


