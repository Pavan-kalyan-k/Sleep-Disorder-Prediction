#!/usr/bin/env python
"""
Dependency Check Script
Verifies that all required packages are installed and working correctly
"""

import sys

def check_imports():
    """Check if all required packages can be imported"""
    
    print("=" * 50)
    print("Checking Required Dependencies")
    print("=" * 50)
    print(f"\nPython Version: {sys.version}")
    print("\n" + "-" * 50)
    
    packages = {
        'streamlit': 'Streamlit',
        'pandas': 'Pandas',
        'numpy': 'NumPy',
        'sklearn': 'Scikit-learn',
        'imblearn': 'Imbalanced-learn',
        'pickle': 'Pickle (built-in)',
    }
    
    all_ok = True
    
    for module_name, display_name in packages.items():
        try:
            if module_name == 'pickle':
                __import__(module_name)
                print(f"✓ {display_name:20} - OK (built-in)")
            else:
                mod = __import__(module_name)
                version = getattr(mod, '__version__', 'unknown')
                print(f"✓ {display_name:20} - OK (v{version})")
        except ImportError as e:
            print(f"✗ {display_name:20} - MISSING")
            all_ok = False
    
    print("\n" + "-" * 50)
    
    if all_ok:
        print("\n✅ All dependencies are installed!")
        print("\nYou can now run the app with:")
        print("   streamlit run app.py")
        return 0
    else:
        print("\n❌ Some dependencies are missing!")
        print("\nTo install all required packages, run:")
        print("   pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    exit_code = check_imports()
    
    # Additional system info
    print("\n" + "-" * 50)
    print("System Information:")
    print(f"Platform: {sys.platform}")
    print(f"Python Executable: {sys.executable}")
    print("-" * 50)
    
    input("\nPress Enter to exit...")
    sys.exit(exit_code)
