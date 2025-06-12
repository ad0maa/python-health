#!/usr/bin/env python3
"""
Simple script to view database contents
"""
import sqlite3
import pandas as pd
from tabulate import tabulate

def view_database():
    """View database tables and contents"""
    try:
        # Connect to the database
        conn = sqlite3.connect('health_app.db')
        
        # Get list of tables
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print("📊 Database: health_app.db")
        print("=" * 50)
        
        if not tables:
            print("❌ No tables found. Make sure the database exists.")
            return
        
        print(f"📋 Tables found: {len(tables)}")
        for table in tables:
            table_name = table[0]
            print(f"\n🗂️  Table: {table_name}")
            print("-" * 30)
            
            # Get table info
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            
            print("Columns:")
            for col in columns:
                col_name, col_type = col[1], col[2]
                print(f"  • {col_name} ({col_type})")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"Rows: {count}")
            
            # Show first few rows if any exist
            if count > 0:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
                rows = cursor.fetchall()
                col_names = [col[1] for col in columns]
                
                print("\nSample data:")
                # Convert None values to 'NULL' for better display
                formatted_rows = []
                for row in rows:
                    formatted_row = ['NULL' if cell is None else str(cell) for cell in row]
                    formatted_rows.append(formatted_row)
                
                print(tabulate(formatted_rows, headers=col_names, tablefmt="grid", maxcolwidths=15))
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    view_database()