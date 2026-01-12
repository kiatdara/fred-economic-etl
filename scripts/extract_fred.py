"""
FRED Data Extraction Script
Extracts economic indicators from Federal Reserve Economic Data (FRED) API
"""

import requests 
import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class FREDExtractor:
    """Extract economic data from FRED API"""
    
    def __init__(self, api_key: str):
        """
        Initialize FRED Extractor
        
        Args:
            api_key: FRED API key
        """
        self.api_key = "39393fe00a33d900f46132b72ff9bae4"
        self.base_url = "https://api.stlouisfed.org/fred"
        
    def get_series_observations(
        self, 
        series_id: str, 
        observation_start: Optional[str] = None,
        observation_end: Optional[str] = None
    ) -> Dict:
        """
        Get observations for a specific FRED series
        
        Args:
            series_id: FRED series ID (e.g., 'GDP', 'UNRATE')
            observation_start: Start date (YYYY-MM-DD)
            observation_end: End date (YYYY-MM-DD)
            
        Returns:
            Dictionary with series data
        """
        endpoint = f"{self.base_url}/series/observations"
        
        params = {
            'series_id': series_id,
            'api_key': self.api_key,
            'file_type': 'json'
        }
        
        if observation_start:
            params['observation_start'] = observation_start
        if observation_end:
            params['observation_end'] = observation_end
            
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Add metadata
            result = {
                'series_id': series_id,
                'extracted_at': datetime.now().isoformat(),
                'count': data.get('count', 0),
                'observations': data.get('observations', [])
            }
            
            print(f"✅ Successfully extracted {result['count']} observations for {series_id}")
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error extracting {series_id}: {str(e)}")
            return {}
    
    def extract_multiple_series(
        self, 
        series_ids: List[str],
        observation_start: Optional[str] = None,
        observation_end: Optional[str] = None
    ) -> Dict[str, Dict]:
        """
        Extract multiple FRED series
        
        Args:
            series_ids: List of FRED series IDs
            observation_start: Start date
            observation_end: End date
            
        Returns:
            Dictionary with all series data
        """
        results = {}
        
        for series_id in series_ids:
            print(f"📊 Extracting {series_id}...")
            data = self.get_series_observations(
                series_id, 
                observation_start, 
                observation_end
            )
            if data:
                results[series_id] = data
                
        return results
    
    def save_to_json(self, data: Dict, filepath: str):
        """
        Save data to JSON file
        
        Args:
            data: Data to save
            filepath: Output file path
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            
        print(f"💾 Data saved to {filepath}")


def main():
    """Main execution function"""
    
    # FRED API Key (replace with your actual key)
    API_KEY = "YOUR_API_KEY_HERE"
    
    # Economic indicators to extract
    SERIES_IDS = [
        'GDP',           # US GDP
        'UNRATE',        # Unemployment Rate
        'CPIAUCSL',      # Consumer Price Index (Inflation)
        'FEDFUNDS',      # Federal Funds Rate
        'DEXTHUS',       # Thailand Baht to USD Exchange Rate
    ]
    
    # Date range (last 5 years)
    START_DATE = "2020-01-01"
    END_DATE = datetime.now().strftime("%Y-%m-%d")
    
    # Initialize extractor
    extractor = FREDExtractor(api_key=API_KEY)
    
    # Extract data
    print("🚀 Starting FRED data extraction...")
    print(f"📅 Date range: {START_DATE} to {END_DATE}")
    print(f"📊 Series: {', '.join(SERIES_IDS)}")
    print("-" * 60)
    
    data = extractor.extract_multiple_series(
        series_ids=SERIES_IDS,
        observation_start=START_DATE,
        observation_end=END_DATE
    )
    
    # Save results
    output_dir = "data/raw"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{output_dir}/fred_data_{timestamp}.json"
    
    extractor.save_to_json(data, output_file)
    
    print("-" * 60)
    print(f"✅ Extraction complete! Extracted {len(data)} series")
    print(f"📁 Output: {output_file}")


if __name__ == "__main__":
    main()