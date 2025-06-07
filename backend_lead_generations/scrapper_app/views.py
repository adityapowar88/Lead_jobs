from django.http import JsonResponse
from .models import Job_Posts
from .scrappers.stepstone import fetch_stepstone_data 
from .scrappers.xing import fetch_xing_data
import traceback

def save_stepstone_jobs(request):
    try:
        jobs = fetch_stepstone_data()
<<<<<<< HEAD
=======
        website = "https://www.stepstone.de"
>>>>>>> ebe54271ce29f739885b798cf0087997138a7cea
        for job in jobs:
            Job_Posts.objects.create(
                lead_title="Scraped via StepStone",
                job_post_url=job.get("url"),
                job_title=job.get("title"),
                company_name=job.get("company"),
<<<<<<< HEAD
=======
                # website=website,
>>>>>>> ebe54271ce29f739885b798cf0087997138a7cea
                person_location=job.get("location")
            )
        return JsonResponse({"status": "success", "message": f"{len(jobs)} StepStone jobs saved."})
    
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({"status": "error", "message": str(e)})


def save_xing_jobs(request):
    try:
        jobs = fetch_xing_data()
        for job in jobs:
            Job_Posts.objects.create(
                lead_title="Scraped via Xing",
                job_post_url=job.get("url"),
                job_title=job.get("title"),
                company_name=job.get("company"),
                person_location=job.get("location")
            )

        return JsonResponse({"status": "success", "message": f"{len(jobs)} Xing jobs saved."})
    
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({"status": "error", "message": str(e)})