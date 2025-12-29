from backend.xray.core import XRayExecution, XRayStep
from backend.xray.store import save_execution

def run_demo_pipeline():
    execution = XRayExecution()

    # STEP 1: Generate Keywords
    step1 = XRayStep(
        step_name="keyword_generation",
        input_data={
            "title": "Steel Water Bottle 32oz",
            "category": "Sports"
        }
    )
    keywords = ["steel water bottle", "insulated bottle 32oz"]
    step1.set_output({"keywords": keywords})
    step1.set_reasoning("Extracted material, size and product type")
    execution.add_step(step1)

    # STEP 2: Candidate Search
    step2 = XRayStep(
        step_name="candidate_search",
        input_data={"keywords": keywords}
    )
    candidates = [
        {"id": "P1", "price": 300, "rating": 3.2, "reviews": 45},
        {"id": "P2", "price": 900, "rating": 4.5, "reviews": 1200},
        {"id": "P3", "price": 1500, "rating": 4.2, "reviews": 300}
    ]
    step2.set_output({"candidates": candidates})
    step2.set_reasoning("Returned mock products from search")
    execution.add_step(step2)

    # STEP 3: Apply Filters
    step3 = XRayStep(
        step_name="apply_filters",
        input_data={"total_candidates": len(candidates)}
    )

    step3.add_rule("min_price", 500)
    step3.add_rule("min_rating", 4)
    step3.add_rule("min_reviews", 100)

    passed = []

    for c in candidates:
        if c["price"] < 500:
            step3.evaluate(c["id"], False, "price below minimum")
        elif c["rating"] < 4:
            step3.evaluate(c["id"], False, "rating below 4")
        elif c["reviews"] < 100:
            step3.evaluate(c["id"], False, "not enough reviews")
        else:
            step3.evaluate(c["id"], True, "passed all filters")
            passed.append(c)

    step3.set_output({
        "passed": len(passed),
        "failed": len(candidates) - len(passed)
    })
    step3.set_reasoning("Filtered products using price, rating and reviews")
    execution.add_step(step3)

    execution.finish()
    save_execution(execution)

    return execution.execution_id
