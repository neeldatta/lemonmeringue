"""
Setup and quick test script for LemonMeringue
"""

import asyncio
import os
import sys
from pathlib import Path

# Add src to path so we can import lemonmeringue
sys.path.insert(0, str(Path(__file__).parent / "src"))

from lemonmeringue import LemonSliceClient, Voices


async def quick_test():
    """Run a quick test to verify everything works"""
    api_key = os.getenv('LEMONSLICE_API_KEY')
    
    if not api_key:
        print("❌ Please set your API key:")
        print("   export LEMONSLICE_API_KEY='your_api_key_here'")
        print("\n   Or on Windows:")
        print("   set LEMONSLICE_API_KEY=your_api_key_here")
        return False
    
    print("🧪 Running quick test...")
    print(f"🔑 API Key: {api_key[:8]}...")
    
    try:
        async with LemonSliceClient(api_key) as client:
            response = await client.quick_generate_text(
                img_url="https://6ammc3n5zzf5ljnz.public.blob.vercel-storage.com/inf2-defaults/cool_man-AZGi3AIjUGN47rGxA8xdHMBGr1Qqha.png",
                voice_id=Voices.ANDREA,
                text="Hello from LemonMeringue! This is a quick test.",
                expressiveness=0.8
            )
        
        print(f"✅ Success! Video generated: {response.video_url}")
        print(f"⏱️  Processing time: {response.processing_time:.1f} seconds")
        print(f"🆔 Job ID: {response.job_id}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def install_dependencies():
    """Install required dependencies"""
    import subprocess
    import sys
    
    print("📦 Installing dependencies...")
    
    try:
        # Install in development mode
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def check_package_structure():
    """Check if package structure is correct"""
    required_files = [
        "src/lemonmeringue/__init__.py",
        "src/lemonmeringue/client.py",
        "setup.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    
    print("✅ Package structure looks good")
    return True


async def main():
    """Main setup and test function"""
    print("🍋 LemonMeringue Setup and Test")
    print("=" * 40)
    
    # Check package structure
    if not check_package_structure():
        print("\n❌ Please make sure all files are in place")
        return
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Failed to install dependencies")
        return
    
    print("\n🧪 Running quick test...")
    
    # Run quick test
    success = await quick_test()
    
    if success:
        print("\n🎉 Setup complete! LemonMeringue is ready to use.")
        print("\n📚 Next steps:")
        print("   1. Run full test suite: python test_all_features.py")
        print("   2. Try the examples in the README")
    else:
        print("\n❌ Setup completed but test failed. Check your API key and connection.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test-only":
        # Just run the test without setup
        asyncio.run(quick_test())
    else:
        # Full setup and test
        asyncio.run(main())