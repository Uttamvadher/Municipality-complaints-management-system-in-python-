from django.db.models.fields import return_None
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import check_password,make_password
from django.utils.timezone import now
from .models import Complaint,User
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import urllib, base64

from django.shortcuts import redirect

def reg(request):
    if request.method == "POST":  
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        token = request.POST.get("token")



        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken!")
            return render(request, 'reg/usr_reg.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'reg/usr_reg.html')
        hashed_password = make_password(password) 

        user = User( 
            username=username,
            email=email,
            phone=phone,
            password=hashed_password,
            token=token


        )

       
        user.save()


        
        messages.success(request, "Registration successful!")
        
        return redirect("login") 
    return render(request, 'reg/usr_reg.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password):  # Check hashed password
            user.last_login = now()
            user.save()
            auth_login(request, user)  # Authenticate the user
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'reg/login.html')
def home(request):
    return render(request,'app/home.html')


def submit_complaint(request):


    if request.method == "POST":
        name =request.POST.get("name")
        department = request.POST.get("department")
        address = request.POST.get("address")
        area = request.POST.get("area")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        description = request.POST.get("description")
        resolved = request.POST.get("resolved")


        complaint=Complaint(
            name=name,
            department=department,
            address=address,
            area=area,
            city=city,
            pincode=pincode,
            description=description,

        )
        if resolved:
            complaint.resolved_at = now().date()

        complaint.save()



        messages.success(request, "Complaint submitted successfully!")
        return redirect("home")

    return render(request, 'app/complaint_form.html')


def analysis(request):

    departments = {
        'Water': 'Water Department',
        'electricity': 'Electricity Department',
        'sanitation': 'Sanitation Department',
        'Road': 'Road Maintenance'
    }



    complaint_counts = {dept: Complaint.objects.filter(department=dept.lower()).count() for dept in departments}
    latest_complaints = Complaint.objects.order_by('-created_at')[:10]




    fig, ax = plt.subplots()
    ax.bar(complaint_counts.keys(), complaint_counts.values(), color=['red', 'blue', 'green', 'yellow'])
    ax.set_xlabel("Departments")
    ax.set_ylabel("Number of Complaints")
    ax.set_title("Number of Complaints per Department")
    plt.xticks(rotation=45, ha="right")

    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart_uri = "data:image/png;base64," + urllib.parse.quote(base64.b64encode(buf.read()).decode())




    fig2, ax2 = plt.subplots()
    ax2.pie(complaint_counts.values(), labels=departments.values(), autopct='%1.1f%%',
            colors=['red', 'blue', 'green', 'yellow'], startangle=90)
    ax2.set_title("Complaint Distribution by Department")


    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    pie_chart_uri = "data:image/png;base64," + urllib.parse.quote(base64.b64encode(buf.read()).decode())

    context = {
        "complaint_counts": complaint_counts,
        "latest_complaints": latest_complaints,

        "chart_uri": chart_uri,
        "pie_chart_uri":pie_chart_uri

    }

    return render(request, "app/analysis.html", context)

def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("login")

from django.conf import settings

PASSWORD = 'Compl@intM@n@g3r1'  

def password_protect(request):
    if request.method == 'POST':
        input_password = request.POST['password']
        if input_password == PASSWORD:
            request.session['authenticated'] = True
            return redirect('view_complaints')
        else:
            return render(request, 'app/password_protect.html', {'error': 'Incorrect password'})
    return render(request, 'app/password_protect.html')

def view_complaints(request):
    if not request.session.get('authenticated'):
        return redirect('password_protect')
    
    complaints = Complaint.objects.all()
    return render(request, 'app/view_complaints.html', {'complaints': complaints})

def mark_resolved(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.is_resolved = True
    complaint.resolved_at = now()
    complaint.save()
    messages.success(request, f"Complaint {complaint.id} marked as resolved.")
    return redirect('view_complaints')