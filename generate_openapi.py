#!/usr/bin/env python3
"""
Script to generate OpenAPI specification for Postman import
"""
import json
from main import app


def generate_openapi_spec():
    """Generate and save OpenAPI specification"""
    openapi_spec = app.openapi()

    # Save to JSON file for Postman import
    with open('openapi.json', 'w') as f:
        json.dump(openapi_spec, f, indent=2)

    print("✅ OpenAPI specification generated successfully!")
    print("📁 File saved as: openapi.json")
    print("\n📋 To import into Postman:")
    print("1. Open Postman")
    print("2. Click 'Import' button")
    print("3. Select 'Upload Files' and choose openapi.json")
    print("4. Postman will create a collection with all API endpoints")

    # Also save a summary of endpoints
    paths = openapi_spec.get('paths', {})
    print(f"\n🔗 Available endpoints ({len(paths)} total):")
    for path, methods in paths.items():
        for method, details in methods.items():
            if method.upper() in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
                summary = details.get('summary', 'No description')
                print(f"  {method.upper():6} {path:30} - {summary}")


if __name__ == "__main__":
    generate_openapi_spec()
