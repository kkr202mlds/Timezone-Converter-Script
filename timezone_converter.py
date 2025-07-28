import argparse
from datetime import datetime
import pytz

def convert_time(time_str, source_tz, target_tz):
    """
    Convert time between timezones
    
    Args:
        time_str: Time string (HH:MM format, 24-hour)
        source_tz: Source timezone (e.g. "America/New_York")
        target_tz: Target timezone (e.g. "Asia/Tokyo")
    
    Returns:
        Converted time string in HH:MM format
    """
    try:
        # Parse time
        hour, minute = map(int, time_str.split(':'))
        today = datetime.now().date()
        source_time = datetime(today.year, today.month, today.day, hour, minute)
        
        # Create timezone objects
        source_zone = pytz.timezone(source_tz)
        target_zone = pytz.timezone(target_tz)
        
        # Localize and convert
        localized = source_zone.localize(source_time)
        converted_time = localized.astimezone(target_zone)
        
        return converted_time.strftime("%H:%M")
    
    except Exception as e:
        raise ValueError(f"Conversion error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert time between timezones')
    parser.add_argument('time', help='Time to convert (HH:MM)')
    parser.add_argument('source', help='Source timezone')
    parser.add_argument('target', help='Target timezone')
    
    args = parser.parse_args()
    
    try:
        result = convert_time(args.time, args.source, args.target)
        print(f"🕒 {args.time} {args.source} → {result} {args.target}")
    except ValueError as e:
        print(f"❌ Error: {str(e)}")
        print("💡 Example valid timezone: 'Asia/Tokyo', 'Europe/London'")
