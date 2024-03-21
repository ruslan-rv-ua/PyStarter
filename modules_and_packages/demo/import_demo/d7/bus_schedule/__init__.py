from .bus_schedule import get_report, save_report

__all__ = ["get_report"]

if __name__ == "__main__":
    save_report(get_report())
