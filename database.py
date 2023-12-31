from sqlalchemy import create_engine, text
import os

db_conn_str = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs_as_dicts = []
    for row in result.all():
      row_dict = row._asdict()  #converting to dict
      jobs_as_dicts.append(row_dict)
    return jobs_as_dicts


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val "),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      job = rows[0]._asdict()
      return job


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO Applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    # Create a dictionary with keys matching the named placeholders in the query
    params = {
      "job_id": job_id,
      "full_name": data['full_name'],
      "email": data['email'],
      "linkedin_url": data['linkedin_url'],
      "education": data['education'],
      "work_experience": data['work_experience'],
      "resume_url": data['resume_url']
    }

    conn.execute(query, params)
