from django.shortcuts import render, redirect
from .models import Marks, Marksheets


# Create your views here.
def home(request):
    return render(request, "landingPage.html")


def index(request):
    if request.method == "POST":
        # Fetch and convert user input
        examination = request.POST.get("examination")
        center = request.POST.get("center")
        semBranch = request.POST.get("semBranch")
        name = request.POST.get("name")
        registrationNo = request.POST.get("registrationNo")

        computer = int(request.POST.get("computer"))
        internal_Computer = int(request.POST.get("internal_Computer"))
        physics = int(request.POST.get("physics"))
        internal_Physics = int(request.POST.get("internal_Physics"))
        mathematics = int(request.POST.get("mathematics"))
        internal_Maths = int(request.POST.get("internal_Maths"))
        electrical_Electronics = int(request.POST.get("electrical_Electronics"))
        internal_Elect_Electronics = int(request.POST.get("internal_Elect_Electronics"))
        practical_Physics = int(request.POST.get("practical_Physics"))
        practical_Eng = int(request.POST.get("practical_Eng"))
        sessional = int(request.POST.get("sessional"))

        sumMarks = computer + physics + mathematics + electrical_Electronics
        sumPractical = practical_Eng + practical_Physics
        sumInternal = (
            internal_Computer
            + internal_Elect_Electronics
            + internal_Maths
            + internal_Physics
        )

        Obtainedtotal = sumMarks + sumInternal + sumPractical

        subTotalComputer = computer + internal_Computer
        subTotalPhysics = physics + internal_Physics
        subTotalMathematics = mathematics + internal_Maths
        subTotalElectrical = electrical_Electronics + internal_Elect_Electronics

        result = "PASS" if Obtainedtotal >= 350 else "FAIL"

        try:
            objMarksheet = Marksheets(
                examination=examination,
                center=center,
                semBranch=semBranch,
                name=name,
                registrationNo=registrationNo,
            )
            objMarksheet.save()

            objMarks = Marks(
                computer=computer,
                internal_Computer=internal_Computer,
                physics=physics,
                internal_Physics=internal_Physics,
                mathematics=mathematics,
                internal_Maths=internal_Maths,
                electrical_Electronics=electrical_Electronics,
                internal_Elect_Electronics=internal_Elect_Electronics,
                practical_Physics=practical_Physics,
                practical_Eng=practical_Eng,
                subTotalComputer=subTotalComputer,
                subTotalPhysics=subTotalPhysics,
                subTotalMathematics=subTotalMathematics,
                subTotalElectrical=subTotalElectrical,
                sessional=sessional,
                total=Obtainedtotal,
                result=result,
            )
            objMarks.save()

            print(
                "DATA FETCHED =>", {"objMarksheet": objMarksheet, "objMarks": objMarks}
            )
            return redirect("display")
        except Exception as e:
            print("Error saving data:", e)

    else:
        return render(request, "index.html")


def display(request):
    print("abc")
    theory = 80
    ia = 20
    physics_Practical = 50
    engineering_drawing = 100

    fetch = Marksheets.objects.all()
    fetchMarks = Marks.objects.all()

    print("DATA AALA")
    for i in fetch:
        marksContext = {
            "examination": i.examination,
            "center": i.center,
            "semBranch": i.semBranch,
            "name": i.name,
            "registrationNo": i.registrationNo,
        }

    for j in fetchMarks:
        dataContext = {
            "computer": j.computer,
            "internal_Computer": j.internal_Computer,
            "physics": j.physics,
            "internal_Physics": j.internal_Physics,
            "mathematics": j.mathematics,
            "internal_Maths": j.internal_Maths,
            "electrical_Electronics": j.electrical_Electronics,
            "internal_Elect_Electronics": j.internal_Elect_Electronics,
            "practical_Physics": j.practical_Physics,
            "practical_Eng": j.practical_Eng,
            "subTotalComputer": j.subTotalComputer,
            "subTotalPhysics": j.subTotalPhysics,
            "subTotalMathematics": j.subTotalMathematics,
            "subTotalElectrical": j.subTotalElectrical,
            "sessional": j.sessional,
            "total": j.total,
            "result": j.result,
        }

    context = {
        "marksContext": marksContext,
        "dataContext": dataContext,
        "theory": theory,
        "ia": ia,
        "physics_Practical": physics_Practical,
        "engineering_drawing": engineering_drawing,
    }
    print(context)
    return render(request, "display.html", context)


def record(request):
    record = Marksheets.objects.all()
    marksRecord = Marks.objects.all()
    content = {"record": record, "marksRecord": marksRecord}
    return render(request, "tableRecord.html", content)


def delete_record(request, id):
    deleteRecord = Marksheets.objects.get(id=id)
    deleteMarks = Marks.objects.get(id=id)
    deleteRecord.delete()
    deleteMarks.delete()
    return redirect("record")


def update_record(request, id):
    records = Marksheets.objects.get(id=id)
    recordMarks = Marks.objects.get(id=id)
    if request.method == "GET":
        context = {"records": records, "recordMarks": recordMarks}
        return render(request, "updateData.html", context)
    else:
        examination = request.POST.get("examination")
        center = request.POST.get("center")
        semBranch = request.POST.get("semBranch")
        name = request.POST.get("name")
        registrationNo = request.POST.get("registrationNo")
        if examination:
            records.examination = examination

        if center:
            records.center = center

        if semBranch:
            records.semBranch = semBranch

        if name:
            records.name = name

        if registrationNo:
            records.registrationNo = registrationNo

        records.save()
        return redirect("record")
