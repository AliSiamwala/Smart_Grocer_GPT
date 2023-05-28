import os
import openai
from flask import Flask, redirect, render_template, request, url_for, session
import pandas as pd


app = Flask(__name__)
app.secret_key = 'some_secret_key' # replace 'some_secret_key' with your own secret key
openai.api_key = os.getenv("OPENAI_API_KEY")


print("Eating the database...")
# # Directory of the Database File: 
# food_Database_2021 = (r'Food_Database\Unabridged DATA.AP.xlsx')
# df = pd.read_excel(food_Database_2021, skiprows=1)
# df.drop(0, inplace=True)
# ## Fill the whole dataframe with 0s
# df = df.fillna(0)

# df[['Food Name','Energy, total metabolisable, available carbohydrate, FSANZ (kcal)']].to_csv(r'Food_Database\first_20rows.csv',index=False)

# calories_df = df.head(10)

# print(calories_df)



# @app.route("/", methods=("GET", "POST"))
# def index():
#     result = None
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=1,
#             max_tokens=150
#         )
#         print(response)
#         session['result'] = response.choices[0].text.strip() # store result in session
#         return redirect(url_for("index"))

#     result = session.get('result') # retrieve result from session
#     return render_template("index.html", result=result)

@app.route("/", methods=("GET", "POST"))
def index():
    result = None
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            prompt=generate_prompt(animal),
            temperature=0.2,
            max_tokens=150
        )
        print(response)
        session['result'] = response.choices[0].message.content # store result in session
        return redirect(url_for("index"))

    result = session.get('result') # retrieve result from session
    return render_template("index.html", result=result)




def generate_prompt(animal):
    return """
    "Stuffing, from chicken, deli cooked",606
    "Bread, gluten free, white, sliced & unsliced, prepacked, composite",919
    "Bread, gluten free, mixed grain, sliced, prepacked, composite",948
    "Bread mix, gluten free, Simple Baking Mix, Healtheries®, fortified vitamins B1 and folate",1420
    "Cracker, corn, ready to eat, Cruskits™, Corn, Arnott's™",1440
    "Cracker, wheat, ready to eat, Salada™, Light, Original, Arnott's™",1440
    "Cracker, mixed grain, ready to eat, Cruskits™, Light, Arnott's™",1440
    "Cracker, mixed grain, ready to eat, Crisp Bread Original, Litebread™, Huntley & Palmers™",1460
    "Cracker, wheat, ready to eat, Cream Crackers, Reduced Fat, Huntley & Palmers™",1520
    "Cracker, rice, plain, composite",1540
    "Cracker, rice, seaweed flavoured, Rice Cracker Seaweed, Sakata®",1440
    "Cracker, rice & seaweed flavoured Rice Cracker Seaweed, Fantastic",1450
    "Cracker, rice & seaweed flavoured, Rice Cracker Seaweed, Pams",1490
    "Biscuit, chocolate chip fudge, ready to eat, Chocolate Chip Fudge, Farmbake™, Arnott's™",2030
    "Biscuit, chocolate chip, ready to eat, Chocolate Chip, Cookie Time®",2040
    "Biscuit, milk chocolate, ready to eat, Milk Chocolate, Arnott's™ & Griffin's™, composite",2060
    "Biscuit, milk chocolate, ready to eat, Tim Tam™, Arnott's™ & Chit Chat™, Griffin's, composite",2170
    "Biscuit, milk chocolate, ready to eat, Double Coat, Tim Tam™, Arnott's™",2220
    "Biscuit, white & dark chocolate, ready to eat, White & Dark Chocolate, Farmbake™, Arnott's™",2080
    "Biscuit, milk chocolate, ready to eat, Double Chocolate, Cookies, Ernest Adams®",2020
    "Biscuit, dark chocolate, ready to eat, Dark Chocolate, Arnott's™ & Wheaten™, Griffin's™, composite",2020
    "Biscuit, dark chocolate, ready to eat, Dark Chocolate, Digestive™, Arnott's™",2070
    "Biscuit, dark chocolate, ready to eat, Dark Chocolate, Wheaten™, Griffin's™",1970
    "Biscuit, milk chocolate, ready to eat, Original, Tim Tam™, Arnott's™",2220
    "Biscuit, milk chocolate, ready to eat, Double Deck Dark Chocolate Delight, Chit Chat™, Griffin's™",2110
    "Biscuit, chocolate chip, ready to eat, Chocolate Chip, Smart, Cookie Time®",1790
    "Biscuit, milk chocolate, ready to eat, Milk Chocolate, Digestives™, Arnott's™",2070
    "Biscuit, milk chocolate, ready to eat, Wheaten™, Griffin's™",2050
    "Biscuit, dark chocolate, ready to eat, Classic Dark, Tim Tam™, Arnott's™",2200
    "Bread, pita, white, composite",1070
    "Bread, gluten free, white, sliced, prepacked, Gluten Free White, Bürgen®",1030
    "Biscuit, short-sweet",2090
    "Bread, gluten free, grain & seed, sliced, prepacked, Gluten Free Ancient Grain & Seeds, Bürgen®",1050
    "Bread, gluten free, seed, sliced, prepacked, Gluten Free 6 Seed, Vogel's®",946
    "Crumpet, white, as purchased, commercial",693
    "Crumpet, white, toasted, commercial",746
    "Bagels, white, plain, as purchased, commercial",1020
    "Bagels, white, plain, toasted, commercial",1090
    "Bread, chapatti or roti, wholemeal, ready to eat, restaurant",1090
    "Bread, naan, white, plain, ready to eat, restaurant",1100
    "Bread roll or bun, white, plain, ready to eat, commercial, fortified folate",1040
    "Bread roll or bun, wholemeal, ready to eat, commercial, fortified folate",960
    "Scone, white, with dates, ready to eat, commercial",1130
    "Scone, white, plain, ready to eat, commercial",1130
    "Scone, white, with cheese, ready to eat, commercial",1210
    "Cake, chocolate, iced, ready to eat, commercial, composite",1590
    "Bread, ciabatta, Italian style, loaf, white wheat flour, plain, as purchased, commercial, composite",1040
    "Bread, ciabatta, Italian style, loaf, white wheat flour, plain, toasted, commercial, composite",1210
    "Bread, French, stick or loaf, from white wheat flour, plain, as purchased, commercial, composite",1130
    "Bread, French, stick or loaf, white wheat flour, plain, toasted, commercial, composite",1440
    "Doughnut, cinnamon & sugar dusted, unfilled, ring shaped, ready to eat, commercial, composite",1660
    "Doughnut, chocolate iced, unfilled, ring shaped, ready to eat, commercial, composite",1660
    "Doughnut, non-chocolate iced, unfilled, ring shaped, ready to eat, commercial, composite",1650
    "Doughnut, cream & jam filled, assorted flavours, ready to eat, commercial, composite",1340
    "Bread, pizza base, thin, from white flour, no topping, as purchased, commercial, composite",1130
    "Bread, pizza base, thick, from white flour, no topping, as purchased, commercial, composite",1090
    "Cake, sponge, plain, unfilled, un-iced,  ready to eat, commercial, composite",1230
    "Cake, assorted fruits, rich or dark, un-iced, ready to eat, commercial, composite",1250
    "Cake, assorted fruits, light, un-iced, ready to eat, commercial, composite",1390
    "Cake, carrot, with icing, ready to eat, commercial, composite",1730
    "Bun, sweet, with dried fruits, spiced, un-iced, commercial, composite",1100
    "Bun, sweet, with chocolate, spiced, un-iced, commercial, composite",1180
    "Bun, sweet, plain, spiced, un-iced, commercial, composite",1000
    "Bread, from white wheat flour, sliced, prepacked, as purchased, commercial, composite",1010
    "Bread, from white wheat flour, sliced, prepacked, toasted, commercial, composite",1220
    "Bread, from wholemeal or wholegrain wheat flour, sliced, prepacked, as purchased, commercial, composite",906
    "Bread, from wholemeal or wholegrain wheat flour, sliced, prepacked, toasted, commercial, composite",1110
    "Bread, from wheatmeal flour, sliced, prepacked, as purchased, commercial, composite",1000
    "Bread, from wheatmeal flour, sliced, prepacked, toasted, commercial, composite",1280
    "Bread, from wheat flour with multigrain, heavy (dense), sliced, prepacked, as purchased, commercial, composite",936
    "Bread, from wheat flour with multigrain, heavy (dense), sliced, prepacked, toasted, commercial, composite",1060
    "Bread, from white wheat flour with multigrain, light, sliced, prepacked, as purchased, commercial, composite",971
    "Bread, from white wheat flour with multigrain, light, sliced, prepacked, toasted, commercial, composite",1180
    "Bread, from wheat flour, soy & linseed added, sliced, prepacked, as purchased, commercial, composite",1090
    "Bread, from wheat flour, soy & linseed added, sliced, prepacked, toasted, commercial, composite",1240
    "Bread, from wheat flour with multigrain & seeds, heavy (dense), sliced, prepacked, as purchased, commercial, composite",1120
    "Bread, from wheat flour with multigrain & seeds, heavy (dense), sliced, prepacked, toasted, commercial, composite",1290
    "Bread, from white wheat flour, seeds added, light, sliced, prepacked, as purchased, commercial, composite",1080
    "Bread, from white wheat flour, seeds added, light, sliced, prepacked, toasted, commercial, composite",1230
    "Bread, from rye flour, sliced, prepacked, as purchased, commercial, composite",772
    "Bread, from rye flour, sliced, prepacked, toasted, commercial, composite",839
    "Wrap, flat bread, from white wheat flour, plain, as purchased, commercial, composite",1150
    "Wrap, flat bread, from white wheat flour, plain, toasted, commercial, composite",1190
    "Wrap, flat bread, from wholemeal wheat flour, as purchased, commercial, composite",1170
    "Wrap, flat bread, from wholemeal wheat flour, toasted, commercial, composite",1220
    "Wrap, flat bread, from wheat flour with multigrain, plain, as purchased, commercial, composite",1180
    "Wrap, flat bread, from wheat flour with multigrain, plain, toasted, commercial, composite",1210
    "Bread, from gluten free flours & sprouted seeds (<10%), sliced, as purchased, commercial, composite",981
    "Bread, from gluten free flours & sprouted seeds (<10%), sliced, toasted, commercial, composite",1090
    "Bread, sourdough, from white wheat flour, loaf, as purchased, commercial, composite",1020
    "Bread, sourdough, from white wheat flour, sliced, toasted, commercial, composite",1150
    "Croissant, from wheat flour, plain, as purchased, commercial, composite",1590
    "Cracker, wheat, ready to eat, Meal Mates™, Griffin's™",1960
    "Croissant, from white wheat flour, plain, toasted, commercial, composite",1690
    "Bread, from sprouted wheat flour, organic, loaf, as purchased, commercial, composite",1090
    "Bread, from sprouted wheat flour, organic, sliced, toasted, commercial, composite",1140
    "Bread, from white wheat flour and banana, loaf, as purchased, commercial, composite",1330
    "Bread, from white wheat flour and banana, sliced, toasted, commercial, composite",1430
    "Muffin split, English style, from white wheat flour, plain, as purchased, commercial, composite",908

    
    ### Instructions ###
    1) Parse the food data above. Each line contains a food item and its caloric value per 100 grams. 
    2) The user will input their caloric requirements. This will be the target value that you aim to reach with the meal plan
    3) Select foods: Randomnly select a number of foods (between 3 and 5) from the list. Calculate the total caloric value for 100 grams of each selected food.
    4) Adjust quantities: If the total caloric value is not within the target range, adjust the quantities of the foods. You can do this by changing the serving size (in grams)
       for each food. Remember that the caloric value provided is for 100 grams, so if you change the serving size to 50 grams, for example, the caloric value would be halved.
    5) Check total calories: Calculate the total caloric intake from the selected foods and their quantities. If the total is within 100 calories of the target, provide the meal
       plan to the user. If not go back to step 3 and adjust the food selection or quantities.
    6) Output: For each selected food, output its name, serving size in grams, and caloric content for the serving size that you have specified. Also provide the total caloric intake.

    Respond in the following way:
    Food 1: (First word of the food), (grams of food)g, (total calories in the food)kcal   
    Food 2: (First word of the food), (grams of food)g, (total calories in the food)kcal
    Food 3: (First word of the food), (grams of food)g, (total calories in the food)kcal
    Food 4: (First word of the food), (grams of food)g, (total calories in the food)kcal
    Food 5: (First word of the food), (grams of food)g, (total calories in the food)kcal
    Total calories: (total calories in the meal plan)kcal

    If the total calories are not within the target range, adjust the food selection or quantities and repeat the process.

    {}
    """.format(
        animal.capitalize()
    )



    # Give the associated foods and the number of calories in the food. Use only the data provided in the list above. Begin response with the input calories.
    # Because each food's calorie number (kcal) in the above list corresponds to that food's caloric value per 100 grams, you MUST provide the number of grams of each food.
    # The total caloric intake of the foods should be within 100 calories of the specified caloric requirements. The number of foods in the list should be 5.
    # to ensure that the user input caloric requirement is met, the assistant should calculate the total caloric intake from the generated food list and ensure it is within the specified range before providing the list. 
    # If the total calories are not within the required range, the assistant should adjust the serving sizes or swap out foods until the total calories meet the requirement.
    # Only print the first word of the food, the grams of the food, and the number of calories in the food for the quantity specified. Write the total amount of calories from the food
    # and the quantities provided.