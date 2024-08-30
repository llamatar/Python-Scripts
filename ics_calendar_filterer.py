# ics_calendar_filterer.py
#
# iCalendar Event Deleter code from https://github.com/maxonary/ics-event-deleter

from typing import List
import icalendar
import re


def main() -> None:
    input_calendar_path = "original_calendar.ics"
    filtered_calendar_path = "filtered_calendar.ics"
    filtered_calendar_deletion_path = "filtered_calendar_deletion.ics"
    ics_preamble = [
        "BEGIN:VCALENDAR",
        # Copy from original calendar export
        "END:VTIMEZONE",
    ]
    # fmt: off
    keywords = [
        'vtuber', 'debut', '3d', 'collab', '[mem]'
        , 'ui', 'うい', 'しぐれうい', 'ui-mama', 'uimama', 'shigure'
        , 'hololive', 'holo'
        , 'holoearth', 'holoearth?', 'yamato'
        , 'holofes', 'holofes4', 'breaking'
        , 'holoshop', 'holomerch', 'buyee'
        , 'yagoo', 'a-chan', 'nodoka'
        , 'sora', 'roboco', 'miko', 'suisei', 'azki'
        , 'aki', 'haachama', 'haato', 'fubuki', 'matsuri'
        , 'shion', 'ayame', 'choco', 'subaru', 'aqua'
        , 'mio', 'korone', 'okayu'
        , 'pekora', 'peko', 'flare', 'noel', 'marine'
        , 'kanata', 'watame', 'towa', 'luna', 'coco'
        , 'lamy', 'nene', 'botan', 'polka', 'aloe'
        , 'la+', 'laplus', 'lui', 'ルイ', 'koyori', 'koyo', 'chloe', 'iroha'
        , 'holoid', 'risu', 'moona', 'iofi'
        , 'ollie', 'anya', 'reine'
        , 'zeta', 'kaela', 'kobo'
        , 'holoen', 'myth', 'calli', 'mori', 'kiara', 'ina', 'gura', 'ame', 'watson'
        , 'council', 'promise', 'irys', 'fauna', 'kronii', 'mumei', 'bae', 'sana'
        , 'holoadvent', 'advent', 'shiori', 'bijou', 'biboo', 'nerissa'
        , 'fuwamoco', 'fwmc', 'fuwawa', 'fww', 'fuwa', 'mococo', 'mcc', 'moco'
        , 'holoen4', 'justice', 'elizabeth', 'erb', 'gigi', 'cecilia', 'raora'
        , 'hiodoshi', 'ao-kun', 'ao', 'kanade', 'ririka', 'raden', 'hajime'
        , 'civia', 'roberu', 'vesper', 'elira', 'pomu', 'yuuhi'
        , 'kson', 'neuro', 'tetel', 'dokibird', 'doki', 'armcha1r'
        , 'holocure', 'asacoco', 'subarudo', 'pekomama', 'mamarissa'
        , 'en&id', 'pekotori', 'korocalli', 'uiwata', 'autofister'
        , 'うい新衣装', 'ルイ３ｄ', '//fwmc', 'okayu,poker', '[mem]fwmc', 'coco\'s', 'fmwc', 'fw/mc', 'tempus2'
    ]
    # fmt: on

    # Import this calendar into new calendar to add the filtered events from original calendar
    create_filtered_calendar(
        keywords, ics_preamble, input_calendar_path, filtered_calendar_path
    )

    # Import this calendar into original calendar to delete the filtered events
    change_ics_entries_to_delete(
        filtered_calendar_path, filtered_calendar_deletion_path
    )


def create_filtered_calendar(
    keywords: List[str],
    ics_preamble: List[str],
    input_calendar_file: str,
    output_calendar_file: str,
) -> None:
    """Creates a calendar file from the events in the input calendar that contain certain keywords."""
    with open(input_calendar_file, "r", encoding="utf8") as input_file:
        input_calendar = icalendar.Calendar.from_ical(input_file.read())

        with open(
            output_calendar_file, "w", encoding="utf8", newline=""
        ) as output_file:
            output_file.write("\r\n".join(ics_preamble) + "\r\n")

            for event in input_calendar.walk("VEVENT"):
                event_summary = event.get("SUMMARY")

                if event_summary and contains_keyword(event_summary, keywords):
                    output_file.write(event.to_ical().decode("utf-8"))

            output_file.write("END:VCALENDAR\r\n")


def contains_keyword(text: str, keywords: List[str]) -> bool:
    """Returns whether any of the keywords are words in the text."""
    words = text.lower().split()
    return any(keyword in words for keyword in keywords)


def change_ics_entries_to_delete(input_file: str, output_file: str) -> None:
    """Creates a calendar file with every event in the input calendar marked for deletion.
    Source: https://github.com/maxonary/ics-event-deleter
    """
    with open(input_file, "r", encoding="utf8") as file:
        ics_content = file.read()

    updated_ics_content = re.sub(
        r"BEGIN:VEVENT.*?END:VEVENT", replace_with_delete, ics_content, flags=re.DOTALL
    )

    with open(output_file, "w", encoding="utf8") as file:
        file.write(updated_ics_content)


def replace_with_delete(match: str) -> str:
    """Replaces event method with CANCEL and status with CANCELLED.
    Source: https://github.com/maxonary/ics-event-deleter
    """
    event = match.group(0)
    uid_match = re.search(r"UID:.*", event)
    if uid_match:
        uid = uid_match.group(0)
        cancel_event = re.sub(r"STATUS:.*\n", "", event)
        cancel_event = re.sub(r"METHOD:.*\n", "", cancel_event)
        cancel_event = cancel_event.replace(
            "BEGIN:VEVENT", "BEGIN:VEVENT\nMETHOD:CANCEL\nSTATUS:CANCELLED"
        )
        return cancel_event
    return event


if __name__ == "__main__":
    main()
