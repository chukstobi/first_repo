# print("Welcome to self diagnosis\nPlease pick symptoms sop we know how best toserve you")
# Headache = input("Do you have headache? Y/N: ").lower()
# if Headache == 'y':
#     vomitting = input("Are you vomitting? Y/N: ").lower()
#     if vomitting == 'y':
#         stooling = input("Are you stooling? Y/N: ").lower()
#         if stooling == "y":
#             print('you have food posining.')
#         else:
#             fever = input("feeling feverish? Y/N: ").lower()
#             if fever == 'y':
#                 print("You have Typhoid.")
#             else:
#                 print("Sickness unknown")
#     else:
#         fever = input("feeling feverish? Y/N: ").lower()
#         if fever == 'y':
#             print("You have malaria.")
#         else:
#             print("Sickness unknown")
# else:
#     print("GoodBye")

malaria_symptoms = ['headache', 'fever', 'cough', 'catarhh','weakness']
Typhoid = ['headache','weakness','abdominal pain','fever']

patient_symptom = []
patient = input("Kindly enter your symptoms: ")
patient2 = patient.split(',')
patient_symptom.append(patient2)

print(patient2 is malaria_symptoms)
print("malaria")
print(patient2)
print(malaria_symptoms)
for j in patient2:
    for l in Typhoid:
        for i in malaria_symptoms:
            if j in i < j in l:
                print("malaria")
            # else:
            #     print("typhoid")
    