{
    'name': "QIS Flight Management",
    'summary': """QIS Flight Management""",
    'description': """Flight management system""",
    'author': "Maduka Sopulu - sperality@gmail.com",
    'version': '1.0.1',
    'depends': ['base', 'contacts'
    ],
    'category': '', # sales, hr
    'data': [
        'security/security_view.xml',
        'security/ir.model.access.csv',
        'views/qis_airline_view.xml',
        'views/booking_view.xml',
        'views/qis_airport_view.xml',
        'views/qis_pilot.xml',],
    "active": False,
    'application': True,
    "sequence": 10
}
