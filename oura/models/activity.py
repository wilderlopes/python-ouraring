from helper import OuraModel, from_json


class Activity(OuraModel):
    _KEYS = [
        "summary_date",
        "day_start",
        "day_end",
        "timezone",
        "score",
        "score_stay_active",
        "score_move_every_hour",
        "score_meet_daily_targets",
        "score_training_frequency",
        "score_training_volume",
        "score_recovery_time",
        "daily_movement",
        "non_wear",
        "rest",
        "inactive",
        "inactivity_alerts",
        "low",
        "medium",
        "high",
        "steps",
        "cal_total",
        "cal_active",
        "met_min_inactive",
        "met_min_low",
        "met_min_medium_plus",
        "met_min_medium",
        "met_min_high",
        "average_met",
        "class_5min",
        "met_1min",
    ]


if __name__ == "__main__":
    test = """
{
        "summary_date": "2016-09-03",
        "day_start": "2016-09-03T04:00:00+03:00",
        "day_end": "2016-09-04T03:59:59+03:00",
        "timezone": 180,
        "score": 87,
        "score_stay_active": 90,
        "score_move_every_hour": 100,
        "score_meet_daily_targets": 60,
        "score_training_frequency": 96,
        "score_training_volume": 95,
        "score_recovery_time": 100,
        "daily_movement": 7806,
        "non_wear": 313,
        "rest": 426,
        "inactive": 429,
        "inactivity_alerts": 0,
        "low": 224,
        "medium": 49,
        "high": 0,
        "steps": 9206,
        "cal_total": 2540,
        "cal_active": 416,
        "met_min_inactive": 9,
        "met_min_low": 167,
        "met_min_medium_plus": 159,
        "met_min_medium": 159,
        "met_min_high": 0,
        "average_met": 1.4375,
        "class_5min":"1112211111111111111111111111111111111111111111233322322223333323322222220000000000000000000000000000000000000000000000000000000233334444332222222222222322333444432222222221230003233332232222333332333333330002222222233233233222212222222223121121111222111111122212321223211111111111111111",
        "met_1min": [ 1.2,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,0.9,0.9,1.2,0.9,1.1,1.2,1.1,1.1,0.9,0.9,0.9,1.1,0.9,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,1.2,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.3,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.3,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.2,0.9,0.9,0.9,1.1,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.9,2.7,2.8,1.6,1.8,1.5,1.5,1.8,1.6,1.9,1.4,1.9,1.4,1.5,1.7,1.7,1.4,1.5,1.5,1.7,1.3,1.7,1.7,1.9,1.5,1.4,1.8,2.2,1.4,1.6,1.7,1.7,1.4,1.5,1.6,1.4,1.4,1.7,1.6,1.3,1.3,1.4,1.3,2.6,1.6,1.7,1.5,1.6,1.6,1.8,1.9,1.8,1.7,2,1.8,2,1.7,1.5,1.3,2.4,1.4,1.6,2,2.8,1.8,1.5,1.8,1.6,1.5,1.8,1.8,1.4,1.6,1.7,1.7,1.6,1.5,1.5,1.8,1.8,1.7,1.8,1.8,1.5,2.4,1.9,1.3,1.2,1.4,1.3,1.5,1.2,1.4,1.4,1.6,1.5,1.6,1.4,1.4,1.6,1.6,1.6,1.8,1.7,1.3,1.9,1.3,1.2,1.2,1.3,1.5,1.4,1.4,1.3,1.7,1.2,1.3,1.5,1.7,1.5,2.6,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.9,3.6,0.9,0.1,0.1,0.1,0.1,0.1,3.3,3.8,3.6,2.3,3.1,3.2,3.5,4.3,3.6,1.7,1.6,2.8,2.1,3.3,4.9,3.3,1.8,5,4.6,5.3,4.9,4.9,5.4,5.4,5.2,5.3,4.5,5.3,4.5,4.4,5,5.3,4.8,4.6,1.8,4.4,3.6,3.5,2.9,2.6,3.1,0.9,0.1,2.9,3.8,1.7,2.8,1.8,1.5,1.4,1.4,1.3,1.4,1.3,1.4,1.3,1.3,1.2,1.3,1.6,1.5,1.5,1.4,1.8,1.3,1.4,1.3,1.4,1.6,1.6,1.4,1.3,1.4,1.4,1.6,1.5,1.4,2,1.5,1.4,1.4,1.3,1.2,1.3,1.3,1.6,1.6,1.5,1.5,1.8,1.5,1.2,1.2,1.5,1.6,1.5,1.7,1.7,1.5,1.6,2.5,1.5,1.3,1.2,1.4,1.6,1.3,1.6,1.7,2,1.2,1.3,1.9,3.3,2.8,1.7,1.4,1.4,1.4,1.5,1.4,1.5,1.3,2,1.4,1.2,1.5,1.2,1.2,1.8,2.4,3,4.6,4,3.6,2.2,0.9,4,3.3,2.6,4.4,2.3,4.5,5.2,5.2,5,5.3,5,4.6,5.4,5.7,5.5,5.2,5.5,3.8,5,5,4.4,4.8,5.5,4.1,4.5,3.2,3.3,2.6,4,3.4,2.1,1.5,1.5,1.4,1.4,1.5,1.3,1.3,1.5,1.4,1.2,1.2,1.4,1.2,1.2,1.2,1.2,1.1,1.3,1.6,1.8,1.5,1.3,1.5,1.5,1.6,1.5,1.6,1.4,1.4,1.4,1.3,1.3,1.3,1.3,1.2,1.3,1.2,1.2,1.2,0.9,1.1,1.1,1.1,1.1,1.7,1.1,0.9,0.9,0.9,1.1,1.1,0.9,1.1,0.9,1.2,1.3,2.4,2.2,1.6,0.9,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,2.4,2.7,1.3,1.4,1.3,1.2,1.3,1.2,1.4,1.4,2.2,1.7,2.9,1.3,1.4,1.2,1.3,1.8,2.1,2.2,2.5,1.9,2.3,2.7,2.3,2,1.7,2,2.1,1.7,1.8,1.2,1.2,0.9,0.9,1.3,1.4,1.2,1.6,1.7,2.4,2.4,2,1.2,1.3,1.3,1.2,1.3,2.4,1.2,1.2,1.3,2,1.3,1.8,1.2,1.2,1.2,1.2,1.8,1.7,1.3,1.3,1.6,1.8,2.2,1.3,1.5,1.5,1.8,1.3,1.7,1.8,2.1,2,1.9,1.6,2,1.8,2,1.6,1.2,1.7,1.5,1.5,2.3,2.6,3.3,3.3,1.5,1.2,1.3,1.5,1.3,1.5,1.5,3.7,2.4,3.3,3,3.7,4.5,2.8,1.3,1.9,2.2,1.6,1.3,1.2,1.3,1.3,2.9,3.3,2,2.2,2.6,2.7,4.5,3.2,4.5,3.3,2.1,3.4,3,2.7,3.3,2.1,2.3,1.7,1.7,2.8,0.9,2.2,0.9,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,1.4,1.6,1.2,1.2,1.3,1.7,1.3,1.5,1.3,1.3,1.3,1.3,1.5,2.9,1.5,1.2,1.4,1.2,1.3,1.3,1.4,1.3,1.4,1.4,1.2,1.2,1.3,1.2,1.2,1.2,1.2,1.4,1.4,1.3,1.2,1.2,1.2,1.9,1.4,1.3,1.4,1.3,1.7,1.3,2.1,2.9,1.9,1.8,1.6,1.4,1.4,1.7,1.2,1.5,1.6,1.9,1.5,1.8,1.3,1.2,1.8,2.3,2,2.2,1.7,1.5,1.2,1.2,1.2,1.1,1.1,1.4,3.3,2,1.5,2.4,2.4,1.6,2.6,2.5,2.3,1.5,1.2,1.2,1.2,1.3,1.2,1.2,1.3,2,1.5,1.7,1.2,1.3,1.6,1.5,1.4,1.4,1.4,1.2,1.2,1.1,1.1,0.9,0.9,1.3,0.9,0.9,0.9,0.9,0.9,1.3,1.1,1.1,1.3,0.9,0.9,1.3,0.9,1.5,2.1,2.1,1.2,1.2,1.3,1.2,1.2,1.5,1.4,1.3,1.2,1.2,1.3,1.3,1.2,1.3,1.2,1.2,1.2,1.2,1.2,1.4,1.2,1.5,1.5,1.4,1.4,1.5,1.5,1.3,1.2,1.2,0.9,2.3,1.8,1.3,1.2,1.2,1.1,0.9,0.9,0.9,1.2,1.6,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,0.9,0.9,0.9,1.9,1.2,1.3,1.1,1.3,1.1,0.9,0.9,0.9,1.2,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,1.1,0.9,0.9,0.9,0.9,1.2,0.9,0.9,0.9,1.1,0.9,0.9,1.2,1.6,1.4,1.3,1.4,1.5,1.2,1.2,1.1,0.9,0.9,1.1,1.1,0.9,0.9,1.1,1.1,0.9,0.9,0.9,0.9,0.9,1.1,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,1.1,1.3,0.9,1.3,1.1,1.1,0.9,1.1,0.9,1.1,0.9,1.3,1.2,0.9,1.1,0.9,0.9,0.9,1.1,0.9,0.9,1.1,1.2,1.6,0.9,1.1,1.4,3.7,2.8,3.2,2.7,1.2,1.2,1.3,1.3,1.3,1.2,1.2,0.9,0.9,0.9,1.1,1.1,0.9,1.1,1.3,0.9,1.1,1.1,1.1,1.3,4.1,1.5,1.7,1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.1,0.9,0.9,0.9,1.1,1.3,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,0.9,0.9,1.1,0.9,0.9,1.1,0.9,0.9,0.9,0.9,0.9,1.1,0.9,0.9,0.9,0.9,0.9,0.9,0.9,1.1,0.9,1.3,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9 ]
    }"""

    activity = from_json(test, Activity)
    print(activity)
