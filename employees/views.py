import requests
import urllib3
from django.shortcuts import render

# Desactiva temporalmente las advertencias de seguridad SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create your views here.
def employee_list(request):
    apiUrl = "https://randomuser.me/api/?results=11"

    try:
        response = requests.get(apiUrl, verify=False)
        if response.status_code == 200:
            data = response.json()
            employees = data['results']
        else:
            employees = []
    except requests.exceptions.RequestException as e:
        # En caso de error, capturar la excepción y devolver una lista vacía
        print(f"Error fetching data from API: {e}")
        employees = []

    return render(request, 'employees/employee_list.html', {'employees': employees})