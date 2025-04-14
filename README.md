Code Space procedure

# Step 1 
docker build -t my-api .

# Step 2
docker run -p 5000:5000 my-api


# Step 3
New Bush
curl "http://localhost:5000/predict?W=1&X=20"


Output：

  "Predicted Engagement Score": 117.16

<img width="864" alt="image" src="https://github.com/user-attachments/assets/d69f48b9-8fb9-4ee1-8ab9-da05e4746524" />
