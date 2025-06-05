from django.http import JsonResponse
from .models import Job_Posts
from .scrappers.stepstone import fetch_stepstone_data  

def save_stepstone_jobs(request):
    try:
        jobs = fetch_stepstone_data()
        website = "https://www.stepstone.de"

        for job in jobs:
            Job_Posts.objects.create(
                lead_title="Scraped via StepStone",
                job_post_url=job.get("url"),
                job_title=job.get("title"),
                company_name=job.get("company"),
                website=website,
                person_location=job.get("location")
            )

        return JsonResponse({"status": "success", "message": f"{len(jobs)} StepStone jobs saved."})
    
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
