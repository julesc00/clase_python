from datetime import datetime


def play_w_datetime():
    opt1 = "RDS snapshot backups at %s...\n" % datetime.now()
    opt2 = f"snapshot-{datetime.now().strftime('%y-%m-%d')}"
    date1 = datetime.now().strftime('%y-%m-%d')
    date_extracted = opt2[9:]

    return f"""
    {opt1}
    {opt2}
    {date_extracted}
    """


if __name__ == "__main__":
    print(play_w_datetime())



