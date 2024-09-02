#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in the WAV header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: %s input.wav output.wav factor\n", argv[0]);
        return 1;
    }

    // Remember filenames and factor
    char *input = argv[1];
    char *output = argv[2];
    float factor = atof(argv[3]);

    // Open input file for reading
    FILE *input_file = fopen(input, "rb");
    if (input_file == NULL)
    {
        printf("Could not open file %s for reading.\n", input);
        return 1;
    }

    // Open output file for writing
    FILE *output_file = fopen(output, "wb");
    if (output_file == NULL)
    {
        printf("Could not open file %s for writing.\n", output);
        fclose(input_file);
        return 1;
    }

    // Allocate memory for the header
    uint8_t header[HEADER_SIZE];

    // Read the header from the input file
    fread(header, sizeof(uint8_t), HEADER_SIZE, input_file);

    // Write the header to the output file
    fwrite(header, sizeof(uint8_t), HEADER_SIZE, output_file);

    // Buffer for reading and writing samples
    int16_t sample;

    // Read samples from input file, scale, and write to output file
    while (fread(&sample, sizeof(int16_t), 1, input_file))
    {
        // Scale the sample
        sample = (int16_t) (sample * factor);

        // Write the scaled sample to the output file
        fwrite(&sample, sizeof(int16_t), 1, output_file);
    }

    // Close files
    fclose(input_file);
    fclose(output_file);

    return 0;
}
