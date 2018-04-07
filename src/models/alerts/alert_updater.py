from src.common.database import Database
from src.models.alerts.alert import Alert
Database.initialize()
alerts = Alert.find_needing_update()



for alert in alerts:
    alert.load_item_price()
    alert.send_email_if_price_reached()