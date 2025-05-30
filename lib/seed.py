#!/usr/bin/env python3

# Script goes here!
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Company, Dev, Freebie, Base

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create Kenyan Developers
devs = [
    Dev(name="Wanjiku Mwangi"),
    Dev(name="Brian Kiprotich"),
    Dev(name="Grace Achieng"),
    Dev(name="Samuel Mwirigi"),
    Dev(name="Faith Njeri"),
    Dev(name="Kevin Ochieng"),
    Dev(name="Lilian Wanjiru"),
    Dev(name="Dennis Kiprop"),
    Dev(name="Rose Akinyi"),
    Dev(name="Collins Omondi"),
    Dev(name="Mary Wambui"),
    Dev(name="Peter Gitau"),
    Dev(name="Agnes Cherop"),
    Dev(name="Joseph Kariuki"),
    Dev(name="Susan Nyokabi"),
    Dev(name="Emmanuel Mutua"),
    Dev(name="Catherine Wanjala"),
    Dev(name="George Kinyua"),
    Dev(name="Eunice Moraa"),
    Dev(name="Daniel Kibet")
]

# Create Kenyan Companies
companies = [
    Company(name="Safaricom", founding_year=1997),
    Company(name="Equity Bank", founding_year=1984),
    Company(name="iHub", founding_year=2010),
    Company(name="Ushahidi", founding_year=2008),
    Company(name="BRCK", founding_year=2013),
    Company(name="Sendy", founding_year=2014),
    Company(name="Twiga Foods", founding_year=2013),
    Company(name="BitPesa", founding_year=2013),
    Company(name="Kopo Kopo", founding_year=2010),
    Company(name="M-Shule", founding_year=2017),
    Company(name="Lynk", founding_year=2015),
    Company(name="Cellulant", founding_year=2003),
    Company(name="Craft Silicon", founding_year=2000),
    Company(name="Angaza", founding_year=2012),
    Company(name="Ajua", founding_year=2016)
]

# Create Freebies with Kenyan context
freebies = [
    # Safaricom freebies
    Freebie(item_name="M-Pesa Branded T-shirt", value=1500, dev=devs[0], company=companies[0]),
    Freebie(item_name="Safaricom Hoodie", value=3500, dev=devs[1], company=companies[0]),
    Freebie(item_name="Power Bank", value=2500, dev=devs[2], company=companies[0]),
    Freebie(item_name="Bluetooth Headphones", value=4500, dev=devs[3], company=companies[0]),
    Freebie(item_name="Branded Water Bottle", value=1200, dev=devs[4], company=companies[0]),
    
    # Equity Bank freebies
    Freebie(item_name="Equity Bank Polo Shirt", value=2000, dev=devs[5], company=companies[1]),
    Freebie(item_name="Laptop Bag", value=3000, dev=devs[6], company=companies[1]),
    Freebie(item_name="Financial Calculator", value=1800, dev=devs[7], company=companies[1]),
    Freebie(item_name="Notebook Set", value=800, dev=devs[8], company=companies[1]),
    
    # iHub freebies
    Freebie(item_name="iHub Innovation T-shirt", value=1500, dev=devs[9], company=companies[2]),
    Freebie(item_name="Tech Startup Stickers", value=500, dev=devs[10], company=companies[2]),
    Freebie(item_name="Coding Bootcamp Certificate", value=50000, dev=devs[11], company=companies[2]),
    Freebie(item_name="Raspberry Pi Kit", value=8000, dev=devs[12], company=companies[2]),
    
    # Ushahidi freebies
    Freebie(item_name="Crisis Mapping Handbook", value=2500, dev=devs[13], company=companies[3]),
    Freebie(item_name="Ushahidi Branded Mug", value=1000, dev=devs[14], company=companies[3]),
    Freebie(item_name="Solar Phone Charger", value=3500, dev=devs[15], company=companies[3]),
    Freebie(item_name="Open Source Contribution Badge", value=0, dev=devs[16], company=companies[3]),
    
    # BRCK freebies
    Freebie(item_name="BRCK Internet Device", value=25000, dev=devs[17], company=companies[4]),
    Freebie(item_name="Kenya Tech Cap", value=1500, dev=devs[18], company=companies[4]),
    Freebie(item_name="Mobile Hotspot", value=8000, dev=devs[19], company=companies[4]),
    Freebie(item_name="Tech Conference Ticket", value=15000, dev=devs[0], company=companies[4]),
    
    # Sendy freebies
    Freebie(item_name="Delivery Backpack", value=4000, dev=devs[1], company=companies[5]),
    Freebie(item_name="GPS Tracker", value=6000, dev=devs[2], company=companies[5]),
    Freebie(item_name="Sendy Branded Jacket", value=3500, dev=devs[3], company=companies[5]),
    Freebie(item_name="Logistics Handbook", value=2000, dev=devs[4], company=companies[5]),
    
    # Twiga Foods freebies
    Freebie(item_name="Farm-to-Market T-shirt", value=1500, dev=devs[5], company=companies[6]),
    Freebie(item_name="Fresh Produce Box", value=2500, dev=devs[6], company=companies[6]),
    Freebie(item_name="Supply Chain Guide", value=1800, dev=devs[7], company=companies[6]),
    Freebie(item_name="Eco-friendly Tote Bag", value=1200, dev=devs[8], company=companies[6]),
    
    # BitPesa freebies
    Freebie(item_name="Blockchain Workshop Access", value=20000, dev=devs[9], company=companies[7]),
    Freebie(item_name="Cryptocurrency Guide", value=2500, dev=devs[10], company=companies[7]),
    Freebie(item_name="FinTech Hoodie", value=3500, dev=devs[11], company=companies[7]),
    Freebie(item_name="Hardware Wallet", value=12000, dev=devs[12], company=companies[7]),
    
    # Kopo Kopo freebies
    Freebie(item_name="Payment Terminal", value=15000, dev=devs[13], company=companies[8]),
    Freebie(item_name="Business Analytics Course", value=25000, dev=devs[14], company=companies[8]),
    Freebie(item_name="SME Growth Toolkit", value=3000, dev=devs[15], company=companies[8]),
    Freebie(item_name="Kopo Kopo Polo Shirt", value=2000, dev=devs[16], company=companies[8]),
    
    # M-Shule freebies
    Freebie(item_name="Educational Tablet", value=18000, dev=devs[17], company=companies[9]),
    Freebie(item_name="E-Learning Subscription", value=5000, dev=devs[18], company=companies[9]),
    Freebie(item_name="EdTech Innovation Award", value=10000, dev=devs[19], company=companies[9]),
    Freebie(item_name="Study Materials Set", value=2500, dev=devs[0], company=companies[9]),
    
    # Lynk freebies
    Freebie(item_name="Gig Economy Handbook", value=2000, dev=devs[1], company=companies[10]),
    Freebie(item_name="Service Provider Kit", value=5000, dev=devs[2], company=companies[10]),
    Freebie(item_name="Lynk Branded Uniform", value=2500, dev=devs[3], company=companies[10]),
    Freebie(item_name="Skills Training Voucher", value=8000, dev=devs[4], company=companies[10]),
    
    # Cellulant freebies
    Freebie(item_name="Mobile Money Integration Guide", value=3000, dev=devs[5], company=companies[11]),
    Freebie(item_name="Payment Gateway Access", value=50000, dev=devs[6], company=companies[11]),
    Freebie(item_name="Cellulant Conference Bag", value=2000, dev=devs[7], company=companies[11]),
    Freebie(item_name="API Documentation Set", value=1500, dev=devs[8], company=companies[11]),
    
    # Craft Silicon freebies
    Freebie(item_name="Banking Software License", value=100000, dev=devs[9], company=companies[12]),
    Freebie(item_name="System Architecture Book", value=4000, dev=devs[10], company=companies[12]),
    Freebie(item_name="Development Environment Setup", value=15000, dev=devs[11], company=companies[12]),
    Freebie(item_name="Craft Silicon Laptop Sleeve", value=2500, dev=devs[12], company=companies[12]),
    
    # Angaza freebies
    Freebie(item_name="Solar Panel Kit", value=35000, dev=devs[13], company=companies[13]),
    Freebie(item_name="Energy Access Report", value=2000, dev=devs[14], company=companies[13]),
    Freebie(item_name="Clean Energy T-shirt", value=1500, dev=devs[15], company=companies[13]),
    Freebie(item_name="Smart Meter Device", value=20000, dev=devs[16], company=companies[13]),
    
    # Ajua freebies
    Freebie(item_name="Customer Engagement Platform Access", value=30000, dev=devs[17], company=companies[14]),
    Freebie(item_name="Data Analytics Course", value=25000, dev=devs[18], company=companies[14]),
    Freebie(item_name="Ajua Branded Hoodie", value=3500, dev=devs[19], company=companies[14]),
    Freebie(item_name="CRM Integration Manual", value=2500, dev=devs[0], company=companies[14]),
    
    # Additional Kenyan-themed freebies
    Freebie(item_name="Maasai Shuka Laptop Bag", value=4000, dev=devs[1], company=companies[0]),
    Freebie(item_name="Kenyan Coffee Subscription", value=6000, dev=devs[2], company=companies[1]),
    Freebie(item_name="Safari Photo Experience", value=25000, dev=devs[3], company=companies[2]),
    Freebie(item_name="Mombasa Beach Resort Voucher", value=30000, dev=devs[4], company=companies[3]),
    Freebie(item_name="Nakuru National Park Pass", value=5000, dev=devs[5], company=companies[4]),
    Freebie(item_name="Kikoy Beach Towel", value=2000, dev=devs[6], company=companies[5]),
    Freebie(item_name="Kenyan Tea Selection", value=3000, dev=devs[7], company=companies[6]),
    Freebie(item_name="Nairobi Tech Hub Membership", value=20000, dev=devs[8], company=companies[7]),
    Freebie(item_name="Mount Kenya Hiking Gear", value=15000, dev=devs[9], company=companies[8]),
    Freebie(item_name="Swahili Language Course", value=8000, dev=devs[10], company=companies[9])
]

# Add all objects to session
session.add_all(devs + companies + freebies)

# Commit all changes
session.commit()

print(f"Successfully seeded database with Kenyan data:")
print(f"- {len(devs)} Kenyan developers")
print(f"- {len(companies)} Kenyan companies") 
print(f"- {len(freebies)} freebies")
print("\nKenyan Companies included:")
for company in companies:
    print(f"  • {company.name} (Founded: {company.founding_year})")

session.close()