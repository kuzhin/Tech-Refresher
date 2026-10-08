
class ReportProcessor:
    """Класс для обработки и сохранения отчетов."""

    def __init__(self, report_data, format_type):
        self.report_data = report_data
        self.format_type = format_type # 'json', 'csv', 'xml'

    def process_report(self):
        """Обрабатывает данные отчета."""
        # ... некоторая логика обработки ...
        processed_data = self.report_data  # упрощенно

        if self.format_type == 'json':
            self._save_to_json(processed_data)
        elif self.format_type == 'csv':
            self._save_to_csv(processed_data)
        elif self.format_type == 'xml':
            self._save_to_xml(processed_data)
        else:
            raise ValueError("Unsupported format")

    def _save_to_json(self, data):
        print(f"Saving {data} to JSON file...")
        # Логика сохранения в JSON

    def _save_to_csv(self, data):
        print(f"Saving {data} to CSV file...")
        # Логика сохранения в CSV

    def _save_to_xml(self, data):
        print(f"Saving {data} to XML file...")
        # Логика сохранения в XML

    def send_report_by_email(self, email):
        """Отправляет отчет по email."""
        print(f"Sending report to {email}...")
        # Логика отправки email