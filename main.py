import tkinter as tk
from tkinter import messagebox
from VectorCalculator import *

def get_vectors():
    vectors = []
    for vector_entry in vector_entries:
        vector_text = vector_entry.get()
        if vector_text:
            try:
                vector = list(map(float, vector_text.split(',')))
                vectors.append(vector)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter vectors as comma-separated numbers")
                return None
    return vectors

def display_result(result):
    if isinstance(result, list):
        result = ', '.join(map(str, result))
    result_label.config(text=f"Result: {result}")

def calculate_sum():
    vectors = get_vectors()
    if vectors:
        result = SumOfVectores(vectors)
        display_result(result)

def calculate_norm():
    vectors = get_vectors()
    if vectors and len(vectors) == 1:
        result = NormOfVector(vectors[0])
        display_result(result)
    else:
        messagebox.showerror("Input Error", "Please enter exactly one vector for the norm calculation")

def calculate_scalar_product():
    vectors = get_vectors()
    if vectors:
        result = ScalarProduct(vectors)
        display_result(result)

def calculate_angle():
    vectors = get_vectors()
    if vectors:
        result = AngleBetweenVectors(vectors)
        display_result(result)

def calculate_cross_product():
    vectors = get_vectors()
    if vectors and len(vectors) == 2:
        result = CrossProduct(vectors)
        display_result(result)
    else:
        messagebox.showerror("Input Error", "Please enter exactly two vectors for the cross product calculation")

def calculate_scalar_triple_product():
    vectors = get_vectors()
    if vectors and len(vectors) == 3:
        result = ScalarTripleProduct(vectors)
        display_result(result)
    else:
        messagebox.showerror("Input Error", "Please enter exactly three vectors for the scalar triple product calculation")

app = tk.Tk()
app.title("Vectorial Calculator")

frame = tk.Frame(app)
frame.pack(pady=10)

vector_entries = []
for i in range(3):
    vector_label = tk.Label(frame, text=f"Vector {i + 1}:")
    vector_label.grid(row=i, column=0)
    vector_entry = tk.Entry(frame, width=30)
    vector_entry.grid(row=i, column=1)
    vector_entries.append(vector_entry)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

sum_button = tk.Button(button_frame, text="Sum", command=calculate_sum)
sum_button.grid(row=0, column=0, padx=5)

norm_button = tk.Button(button_frame, text="Norm", command=calculate_norm)
norm_button.grid(row=0, column=1, padx=5)

scalar_product_button = tk.Button(button_frame, text="Scalar Product", command=calculate_scalar_product)
scalar_product_button.grid(row=0, column=2, padx=5)

angle_button = tk.Button(button_frame, text="Angle", command=calculate_angle)
angle_button.grid(row=1, column=0, padx=5)

cross_product_button = tk.Button(button_frame, text="Cross Product", command=calculate_cross_product)
cross_product_button.grid(row=1, column=1, padx=5)

scalar_triple_product_button = tk.Button(button_frame, text="Scalar Triple Product", command=calculate_scalar_triple_product)
scalar_triple_product_button.grid(row=1, column=2, padx=5)

result_label = tk.Label(app, text="Result: ")
result_label.pack(pady=10)

app.mainloop()