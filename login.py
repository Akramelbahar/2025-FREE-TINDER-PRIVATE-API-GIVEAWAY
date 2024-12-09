import tls_client
import json
from datetime import datetime, timedelta
import time
import uuid

requests = tls_client.Session(client_identifier="chrome_120")
headers = {
    "host": "gaia-server.rosettastone.com",
    "accept": "*/*",
    "authorization": "Bearer 184162e1-bd5c-4265-966c-00362c9b6793",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "origin": "https://learn.rosettastone.com",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
}

def addProgress(userId, courseId, sequenceId, activityId, activityAttemptId, activityStepId, activityStepAttemptId):
    url = "https://gaia-server.rosettastone.com/graphql"
    current_time = datetime.utcnow()
    end_timestamp = current_time + timedelta(milliseconds=100, seconds=26)
    end_timestamp_iso = end_timestamp.isoformat() + "Z"
    p1 =  {
  "operationName": "AddUsageOverhead",
  "variables": {
                "messages": [
                {
                    "id": str(uuid.uuid4()),
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                    "learningContext": courseId,
                    "durationMs": 22133,
                    "endTimestamp": end_timestamp_iso
                }
                ]
            },
            "query": "mutation AddUsageOverhead($messages: [UsageOverheadMessage!]!) {\n  usageOverhead(messages: $messages)\n}\n"
            }
    print(requests.post(url , headers , p1).text)
    current_time = datetime.utcnow()
    end_timestamp = current_time + timedelta(milliseconds=100, seconds=10)
    end_timestamp_iso = end_timestamp.isoformat() + "Z"
    payload = {
        "operationName": "AddProgress",
        "variables": {
            "userId": userId,
            "messages": [
                {
                    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                    "courseId": courseId,
                    "sequenceId": sequenceId,
                    "version": 1,
                    "activityId": activityId,
                    "activityAttemptId": activityAttemptId,
                    "activityStepId": activityStepId,
                    "activityStepAttemptId": activityStepAttemptId,
                    "answers": [],
                    "score": 0,
                    "skip": True,
                    "durationMs": 5000,
                    "endTimestamp": end_timestamp_iso
                }
            ]
        },
        "query": "mutation AddProgress($userId: String, $messages: [ProgressMessage!]!) {\n  progress(userId: $userId, messages: $messages) {\n    id\n    __typename\n  }\n}\n"
    }
   
    try:
        resp = requests.post(url, headers=headers, json=payload)
        print(f"Progress added: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"Error in addProgress: {e}")
    time.sleep(5)

def getProgress(courseId="0f51efd0bd4974e0377b42dab3b4fdd7"):
    url = "https://gaia-server.rosettastone.com/graphql"
    payload = {
        "operationName": "getProgress",
        "variables": {"courseId": courseId},
        "query": "query getProgress($courseId: String) {\n  progress(courseId: $courseId) {\n    ...ProgressDetails\n    __typename\n  }\n}\n\nfragment ProgressDetails on ProgressCourse {\n  id\n  courseId\n  countOfSequencesInCourse\n  percentComplete\n  sequences {\n    id\n    sequenceId\n    version\n    percentComplete\n    bestGrade\n    countOfActivities\n    activities {\n      id\n      activityId\n      percentComplete\n      bestGrade\n      attempts {\n        id\n        activityAttemptId\n        steps {\n          id\n          activityStepId\n          attempts {\n            id\n            activityStepAttemptId\n            score\n            skipped\n            endTimestamp\n            answers {\n              answer\n              correct\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
    }

    try:
        resp = requests.post(url, json=payload, headers=headers)
        data = resp.json().get("data", {}).get("progress", [])
        
        for course in data:
            userId = "2ae25802-b158-48a4-b11f-79e708245f33"
            for sequence in course.get("sequences", []):
                sequenceId = sequence.get("sequenceId")
                for activity in sequence.get("activities", []):
                    activityId = activity.get("id")
                    for attempt in activity.get("attempts", []):
                        activityAttemptId = attempt.get("id")
                        for step in attempt.get("steps", []):
                            activityStepId = step.get("id")
                            for stepAttempt in step.get("attempts", []):
                                activityStepAttemptId = stepAttempt.get("id")
                                addProgress(
                                    userId, courseId, sequenceId, activityId,
                                    activityAttemptId, activityStepId, activityStepAttemptId
                                )
    except Exception as e:
        print(f"Error in getProgress: {e}")

getProgress()
