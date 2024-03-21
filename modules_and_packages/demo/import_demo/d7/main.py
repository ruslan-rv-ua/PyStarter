from bus_schedule import get_report, save_report

report = get_report()
save_report(report, 'bus_schedule.json')
