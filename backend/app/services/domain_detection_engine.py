from collections import Counter


class DomainDetectionEngine:

    def generate(self, workbook):

        context = workbook.get(
            "workbook_context",
            {}
        )

        semantic_frequency = context.get(
            "semantic_frequency",
            {}
        )

        dataset_types = context.get(
            "dataset_types",
            []
        )

        worksheets = workbook.get(
            "worksheets",
            []
        )

        domain = {

            "name": "General",

            "confidence": 0,

            "scores": {},

            "industry": "General",

            "description": "",

            "primary_dataset": ""

        }

        scores = Counter()

        # --------------------------------------------------
        # Dataset Type Detection
        # --------------------------------------------------

        for dataset in dataset_types:

            text = str(dataset).lower()

            if "sales" in text:

                scores["Sales"] += 10

            elif "finance" in text:

                scores["Finance"] += 10

            elif "employee" in text or "hr" in text:

                scores["HR"] += 10

            elif "inventory" in text:

                scores["Inventory"] += 10

            elif "purchase" in text:

                scores["Procurement"] += 10

            elif "project" in text:

                scores["Project"] += 10

            elif "hospital" in text:

                scores["Healthcare"] += 10

            elif "student" in text:

                scores["Education"] += 10

            elif "shipping" in text:

                scores["Logistics"] += 10

        # --------------------------------------------------
        # Semantic Detection
        # --------------------------------------------------

        for semantic, count in semantic_frequency.items():

            semantic = semantic.lower()

            if semantic == "currency":

                scores["Sales"] += count * 2
                scores["Finance"] += count * 2

            elif semantic == "customer":

                scores["Sales"] += count * 3

            elif semantic == "product":

                scores["Sales"] += count * 2
                scores["Inventory"] += count * 2

            elif semantic == "quantity":

                scores["Inventory"] += count * 2

            elif semantic == "person":

                scores["HR"] += count * 3

            elif semantic == "location":

                scores["Logistics"] += count * 2

            elif semantic == "vendor":

                scores["Procurement"] += count * 3

            elif semantic == "project":

                scores["Project"] += count * 3

        # --------------------------------------------------
        # Worksheet Name Detection
        # --------------------------------------------------

        for sheet in worksheets:

            name = sheet.get(
                "sheet_name",
                ""
            ).lower()

            if "sales" in name:

                scores["Sales"] += 5

            elif "finance" in name:

                scores["Finance"] += 5

            elif "employee" in name or "hr" in name:

                scores["HR"] += 5

            elif "inventory" in name:

                scores["Inventory"] += 5

            elif "purchase" in name:

                scores["Procurement"] += 5

            elif "project" in name:

                scores["Project"] += 5

        # --------------------------------------------------
        # Final Decision
        # --------------------------------------------------

        if scores:

            best = scores.most_common(1)[0]

            domain["name"] = best[0]

            total = sum(scores.values())

            if total > 0:

                domain["confidence"] = round(

                    (best[1] / total) * 100,

                    2

                )

        # --------------------------------------------------
        # Industry Description
        # --------------------------------------------------

        descriptions = {

            "Sales":
            "Sales analytics and commercial performance.",

            "Finance":
            "Financial reporting and accounting analytics.",

            "HR":
            "Human resource and workforce analytics.",

            "Inventory":
            "Inventory optimization and stock management.",

            "Logistics":
            "Supply chain and logistics operations.",

            "Procurement":
            "Procurement and vendor management.",

            "Project":
            "Project planning and execution analytics.",

            "Healthcare":
            "Healthcare operational analytics.",

            "Education":
            "Education and student performance analytics.",

            "General":
            "General business intelligence."
        }

        domain["industry"] = domain["name"]

        domain["description"] = descriptions.get(

            domain["name"],

            descriptions["General"]

        )

        if dataset_types:

            domain["primary_dataset"] = dataset_types[0]

        domain["scores"] = dict(scores)

        workbook["domain"] = domain

        return workbook