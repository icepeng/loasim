from loasim.job.artist import lostark_job_artist
from loasim.job.base import Job, SkillSpecification, SkillState, Tripod
from loasim.job.blade import lostark_job_blade
from loasim.job.hawkeye import lostark_job_hawkeye
from loasim.job.scouter import lostark_job_scouter

job_dict = {
    "artist": lostark_job_artist,
    "blade": lostark_job_blade,
    "hawkeye": lostark_job_hawkeye,
    "scouter": lostark_job_scouter,
}


def get_job(job_name: str) -> Job:
    job = job_dict[job_name]
    if job is None:
        raise ValueError(f"{job_name} is not supported")
    return job
