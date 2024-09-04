def expand_field(field, max_value):
    if field == '*':
        return list(range(max_value + 1))
    
    values = set()
    for part in field.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            values.update(range(start, end + 1))
        elif '/' in part:
            base, step = part.split('/')
            if base == '*':
                base = 0
            else:
                base = int(base)
            step = int(step)
            values.update(range(base, max_value + 1, step))
        else:
            values.add(int(part))
    
    return sorted(values)

def parse_cron_expression(expression):
    fields = expression.split()
    if len(fields) < 5 or len(fields) > 6:
        raise ValueError("Invalid cron expression format")
    
    minute = expand_field(fields[0], 59)
    hour = expand_field(fields[1], 23)
    day_of_month = expand_field(fields[2], 31)
    month = expand_field(fields[3], 12)
    day_of_week = expand_field(fields[4], 6)
    year = expand_field(fields[5], 9999) if len(fields) > 5 else None
    
    return {
        'minute': minute,
        'hour': hour,
        'day_of_month': day_of_month,
        'month': month,
        'day_of_week': day_of_week,
        'year': year
    }

# Example usage
cron_expression = "30 8 * * 1-5"
parsed_expression = parse_cron_expression(cron_expression)
print(parsed_expression)
