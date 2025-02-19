import yaml
from typing import Union, Dict
from dataclasses import dataclass

@dataclass
class Config:
    # Required paths
    input_path: str
    output_path: str
    
    # Tile customization
    desired_size: int = 256
    desired_magnification: int = 20
    overlap: int = 1
    
    # Preprocessing options
    remove_blurry_tiles: bool = False
    normalize_staining: bool = False
    encode: bool = False
    
    # Thresholds
    tissue_threshold: float = 0.7
    blur_threshold: float = 0.015
    min_tiles: float = 0
    
    # Device settings
    device: Union[str, None] = None
    gpu_processes: int = 1
    cpu_processes: Union[int, None] = None

def load_config(config_path: str = None, args = None) -> Config:
    """
    Load configuration from YAML file and/or command line arguments.
    Command line arguments take precedence over YAML config.
    """
    # Default config
    config_dict = {}
    
    # Load YAML config if provided
    if config_path:
        try:
            with open(config_path, 'r') as f:
                yaml_dict = yaml.safe_load(f)
                if yaml_dict:  # Only update if not None
                    config_dict.update(yaml_dict)
        except Exception as e:
            print(f"Warning: Could not load config file: {e}")
    
    # Update with command line arguments if provided
    if args:
        # Convert args namespace to dictionary, excluding None values and 'config' argument
        args_dict = {k: v for k, v in vars(args).items() if v is not None and k != 'config'}
        config_dict.update(args_dict)
    
    # Create Config object
    return Config(**config_dict)