def identify_dataset(columns):

    cols = [c.lower() for c in columns]

    if any(word in cols for word in [
        "product",
        "qty",
        "quantity",
        "amount",
        "sales",
        "price"
    ]):
        return "Sales"

    elif any(word in cols for word in [
        "employee",
        "department",
        "salary",
        "designation"
    ]):
        return "HR"

    elif any(word in cols for word in [
        "invoice",
        "vendor",
        "gst",
        "tax"
    ]):
        return "Finance"

    elif any(word in cols for word in [
        "candidate",
        "interview",
        "recruiter"
    ]):
        return "Recruitment"

    elif any(word in cols for word in [
        "vessel",
        "container",
        "port",
        "shipment"
    ]):
        return "Shipping"

    return "Unknown"