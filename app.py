import pickle


reportCards = []


def writeToFile():
    pickle.dump(reportCards, open('data.dat', 'wb+'))

def loadFromFile():
    global reportCards
    try:
        reportCards = pickle.load(open('data.dat', 'rb+'))
        
    except Exception:
        reportCards = []



def addNewReportCard():
    report_card_dict = {
        "id": len(reportCards) + 1,
        "exam_name" : input("Enter Exam Name: "),
        "student_name" : input("Enter Student's Name: "),
        "student_addmission_number": input("Enter Student's Admission Number: "),
        "student_class": input("Enter Student's class: "),
        "student_section": input("Enter Student's section: "),
        "total_marks": round(float(input("Enter Total Marks: ")), 2),
        "total_marks_obtained": round(float(input("Enter Marks Obtained : ")), 2),
    }

    reportCards.append(report_card_dict)

    print('Report Card Added')





menu = '''
    1. Add New Report Card
    2. Edit Report Card
    3. View Report Card
    4. Delete Report Card
    0. Exit
    '''

if __name__ == '__main__':

    loadFromFile()

    choice = None

    while choice != 0:
        
        print(menu)
        choice = int(input('Enter Choice: '))

        if choice == 0:
            writeToFile()
            exit()
        
        if choice == 1:
            addNewReportCard()