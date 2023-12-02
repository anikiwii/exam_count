import PyPDF2

def count_points(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize the sum of points
        total_points = 0

        # Iterate through the PDF pages
        for page_num in range(len(pdf_reader.pages)):
            # Extract text from the current page
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Assume that points are written in the format "Points: X/Y"
            # Where X is the earned points, and Y is the maximum points for the task
            index_start = text.find("Points:")
            if index_start != -1:
                index_end = text.find("/", index_start)
                if index_end != -1:
                    points = int(text[index_start + len("Points:"):index_end])
                    total_points += points

        return total_points


def evaluate_program(pdf_path):
    # Count points from the PDF file
    total_points = count_points(pdf_path)

    # Calculate the percentage of earned points
    percentage = (total_points / 70) * 100

    # Check the grade
    if percentage >= 51:
        return "Passed with a Grade 3."
    else:
        return "Not passed."


# Sample usage
pdf_path = 'path/to/your/file.pdf'
result = evaluate_program(pdf_path)
print(result)