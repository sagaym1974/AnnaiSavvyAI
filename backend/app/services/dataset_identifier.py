def identify_dataset(columns):

    columns = [

        str(column).lower().strip()

        for column in columns

    ]

    scores = {

        "Sales": 0,

        "Finance": 0,

        "HR": 0,

        "Inventory": 0,

        "Procurement": 0,

        "Project": 0,

        "Recruitment": 0,

        "Shipping": 0,

        "Logistics": 0,

        "Healthcare": 0,

        "Education": 0

    }

    keywords = {

        "Sales": [

            "sales",

            "sale",

            "customer",

            "client",

            "product",

            "item",

            "price",

            "amount",

            "revenue",

            "profit",

            "margin",

            "discount",

            "invoice",

            "order"

        ],

        "Finance": [

            "finance",

            "account",

            "ledger",

            "expense",

            "income",

            "salary",

            "payment",

            "receipt",

            "cash",

            "bank",

            "gst",

            "cgst",

            "sgst",

            "igst",

            "tax",

            "balance"

        ],

        "HR": [

            "employee",

            "emp",

            "staff",

            "department",

            "designation",

            "attendance",

            "leave",

            "payroll",

            "joining",

            "manager"

        ],

        "Inventory": [

            "inventory",

            "stock",

            "warehouse",

            "quantity",

            "qty",

            "opening stock",

            "closing stock",

            "reorder",

            "batch"

        ],

        "Procurement": [

            "purchase",

            "vendor",

            "supplier",

            "quotation",

            "po",

            "purchase order",

            "material"

        ],

        "Project": [

            "project",

            "task",

            "milestone",

            "activity",

            "resource"

        ],

        "Recruitment": [

            "candidate",

            "resume",

            "recruiter",

            "interview",

            "hiring",

            "offer"

        ],

        "Shipping": [

            "vessel",

            "container",

            "shipment",

            "port",

            "bl",

            "bill of lading",

            "voyage"

        ],

        "Logistics": [

            "dispatch",

            "delivery",

            "transport",

            "truck",

            "route",

            "consignment"

        ],

        "Healthcare": [

            "patient",

            "doctor",

            "hospital",

            "medicine",

            "diagnosis",

            "treatment"

        ],

        "Education": [

            "student",

            "teacher",

            "subject",

            "course",

            "exam",

            "marks",

            "grade"

        ]

    }

    for column in columns:

        for dataset, words in keywords.items():

            for word in words:

                if word in column:

                    scores[dataset] += 1

    best_dataset = max(

        scores,

        key=scores.get

    )

    if scores[best_dataset] == 0:

        return "General"

    return best_dataset