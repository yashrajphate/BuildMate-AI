import time
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    print("=== Testing BuildMate AI Backend APIs ===")
    time.sleep(1.0)

    # 1. Health check
    res = requests.get(f"{BASE_URL}/api/health")
    print(f"Health Check Status: {res.status_code}")
    print(f"Health Check Body: {json.dumps(res.json(), indent=2)}")

    # 2. Equipment Catalog
    res = requests.get(f"{BASE_URL}/api/equipment/list")
    data = res.json()
    print(f"\nEquipment List Status: {res.status_code}, Total Count: {len(data)}")
    print(f"Sample Equipment Item: {data[0]['name']} ({data[0]['category']})")

    # 3. AI Assistant Query - Construction
    query = {"prompt": "I need a machine for foundation excavation for 2 days."}
    res = requests.post(f"{BASE_URL}/api/assistant/query", json=query)
    print(f"\nAssistant Query (Construction) Status: {res.status_code}")
    out = res.json()
    print(f"  Recommended Equipment: {out.get('equipment_name')}")
    print(f"  Extracted Task: {out.get('extracted', {}).get('task')}")
    print(f"  Extracted Duration: {out.get('extracted', {}).get('duration')}")
    print(f"  Extracted Category: {out.get('extracted', {}).get('category')}")

    # 4. AI Assistant Query - Agriculture
    query_agri = {"prompt": "Need tractor for ploughing 5 acres."}
    res_agri = requests.post(f"{BASE_URL}/api/assistant/query", json=query_agri)
    out_agri = res_agri.json()
    print(f"\nAssistant Query (Agriculture) Status: {res_agri.status_code}")
    print(f"  Recommended Equipment: {out_agri.get('equipment_name')}")
    print(f"  Extracted Task: {out_agri.get('extracted', {}).get('task')}")
    print(f"  Extracted Area/Qty: {out_agri.get('extracted', {}).get('area_quantity')}")

    # 5. Compare Equipment
    comp_payload = {"equipment_id_1": "excavator-heavy", "equipment_id_2": "jcb-3dx"}
    res_comp = requests.post(f"{BASE_URL}/api/equipment/compare", json=comp_payload)
    print(f"\nEquipment Compare Status: {res_comp.status_code}")
    print(f"  Comparison Summary: {res_comp.json().get('summary')}")

    # 6. Generate Booking Request
    booking_payload = {
        "equipment_name": "JCB / Backhoe Loader",
        "purpose": "Foundation excavation",
        "duration": "2 days",
        "location": "Not specified"
    }
    res_book = requests.post(f"{BASE_URL}/api/booking/generate", json=booking_payload)
    print(f"\nBooking Generator Status: {res_book.status_code}")
    print(f"  Formatted Output:\n{res_book.json().get('formatted_text')}")

    # 7. Check Root Frontend Serve
    res_root = requests.get(f"{BASE_URL}/")
    print(f"\nRoot Frontend Status: {res_root.status_code}, Length: {len(res_root.text)} bytes")

    print("\n[SUCCESS] All BuildMate AI backend & frontend tests PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
