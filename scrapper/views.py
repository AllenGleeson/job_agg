from django.http import JsonResponse

def get_jobs(request):
    jobs = [
        {"title": "Software Engineer", "company": "Google", "location": "New York", "posted_date": "2024-09-10"},
        {"title": "Data Scientist", "company": "Facebook", "location": "San Francisco", "posted_date": "2024-09-08"},
        {"title": "Backend Developer", "company": "Microsoft", "location": "Seattle", "posted_date": "2024-09-05"},
    ]
    return JsonResponse(jobs, safe=False)