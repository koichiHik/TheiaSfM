
import subprocess

IMAGE_DIRECTORY = \
    "/home/koichi/Okinawa_Pic/Kokusai_Dori_20190525/"
IMAGE_EXTENSION = "*.JPG"

CAMERA_CALIB_FILE = "calib.json"

# Build Reconstruction Settings.
BUILD_RECONSTRUCTION_BIN = "../../build/bin/build_reconstruction"
BUILD_RECONSTRUCTION_FLAGFILE = "../flagfiles/build_reconstruction_flags.txt"
BUILD_RECONSTRUCTION_INPUT_PATH = IMAGE_DIRECTORY + IMAGE_EXTENSION
BUILD_RECONSTRUCTION_CALIB_PATH = IMAGE_DIRECTORY + CAMERA_CALIB_FILE
BUILD_RECONSTRUCTION_OUTPUT_PATH = IMAGE_DIRECTORY + "reconstruction"


# Colorize Settings.
COLORIZE_RECONSTRUCTION_BIN = "../../build/bin/colorize_reconstruction"
COLORIZE_RECONSTRUCTION_OUTPUT_PATH = \
    IMAGE_DIRECTORY + "colorize_reconstruction"

# Ply file settings.
PLYFILE_CONVERTER_BIN = "../../build/bin/write_reconstruction_ply_file"
PLYOUTPUT_FILEPATH = IMAGE_DIRECTORY + "reconstruction.ply"


if __name__ == "__main__":
    print(__file__)

    # Reconstuction from images.
    subprocess.call(
        [BUILD_RECONSTRUCTION_BIN,
         "-flagfile", BUILD_RECONSTRUCTION_FLAGFILE,
         "-images", BUILD_RECONSTRUCTION_INPUT_PATH,
         "-calibration_file", BUILD_RECONSTRUCTION_CALIB_PATH,
         "-output_reconstruction", BUILD_RECONSTRUCTION_OUTPUT_PATH])

    # Colorize reconstruction.
    subprocess.call(
        [COLORIZE_RECONSTRUCTION_BIN,
         "-image_directory", IMAGE_DIRECTORY,
         "-input_reconstruction_file", BUILD_RECONSTRUCTION_OUTPUT_PATH + "-0",
         "-output_reconstruction_file", COLORIZE_RECONSTRUCTION_OUTPUT_PATH,
         "-num_threads", str(16)])

    # Convert to ply files.
    subprocess.call(
        [PLYFILE_CONVERTER_BIN,
         "-reconstruction", COLORIZE_RECONSTRUCTION_OUTPUT_PATH,
         "-ply_file", PLYOUTPUT_FILEPATH,
         "-min_num_observations_per_point", str(2)])
