# inserisci il peso
# confronta il peso
# se il peso è sotto 18.5 è sottopeso
# se è tra 18.5 e sotto i 25 il peso è normale
# sopra i 25 ma sotto i 30 è sovrappeso
# fra i 30 e i 35 è obeso
# sopra i 35 è clinicamente obeso

#inserisci il peso
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

#il resto delle operazioni

#calcola il body mass index (BMI)

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"your BMI is: {bmi} and You are underwight")
elif bmi < 25:
    print(f"your BMI is: {bmi} and Your wight is normal")
elif bmi < 30:
    print(f"your BMI is: {bmi} and You are overwight")
elif bmi < 35:
    print(f"your BMI is: {bmi} and You are obese")
else:
    print(f"your BMI is: {bmi} and You are clinically obese")

     
