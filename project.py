import streamlit as st

def reset_number_input_water():
    st.session_state.showers_min = 0
    st.session_state.num_toilet = 0
    st.session_state.num_brush = 0
    st.session_state.dish_wash_min = 0
    st.session_state.num_laundry = 0
    st.session_state.watering_garden_min = 0
def reset_number_input_waste():
    st.session_state.plastic = 0.0
    st.session_state.paper = 0.0
    st.session_state.glass = 0.0
    st.session_state.metal = 0.0
    st.session_state.organic = 0.0
    st.session_state.other = 0.0
    st.session_state.recycled = 0.0

def water_usage_calculator():
    st.subheader("Water Usage Calculator")
    # User inputs
    showers_min = st.number_input("Enter the number of minutes spent in the shower per day", min_value=0, value=0,key="showers_min")
    num_toilet = st.number_input("Enter the number of toilet flushes per day",min_value=0, value=0,key="num_toilet")
    num_brush = st.number_input("Enter the number of times you brush your teeth per day",min_value=0, value=0,key="num_brush")
    dish_wash_min = st.number_input("Enter the number of minutes spent hand-washing dishes per day",min_value=0,value=0,key="dish_wash_min")
    num_laundry = st.number_input("Enter the number of laundry loads per week",min_value=0, value=0,key="num_laundry")
    watering_garden_min = st.number_input("Enter the number of minutes spent watering your garden per day",min_value=0, value=0,key="watering_garden_min")
    
   
    # Calculate water usage
    if st.button("Calculate"):
        total = (showers_min*9)+(num_toilet*6)+(num_brush*1.5)+(dish_wash_min*12)+(num_laundry*80/7)+(watering_garden_min*15)
        st.subheader(f"\nTotal daily water usage: {total:.2f} liters")
        if total > 300:
            st.subheader("\nYour water usage is above average. Consider implementing water-saving measures.")
       
        st.subheader("\n!!! Here are some tips to help you reduce your water usage:")
        st.write()
        st.write("Fix leaks: A small drip can waste gallons of water daily.")
        st.write("Install water-saving fixtures: Use low-flow showerheads and faucets.")
        st.write("Take shorter showers: Reduce your shower time to save water.")
        st.write("Turn off the tap: Don’t let the water run while brushing your teeth or washing dishes.")
        st.write("Use a broom: Sweep driveways and sidewalks instead of hosing them down.")
        st.write("Collect rainwater: Use it to water your garden or wash your car.")
        st.write("Only run full loads: Use your dishwasher and washing machine with full loads only.")
    button = st.button("Reset", on_click=reset_number_input_water)
            


def waste_reduction_and_recycling():
    st.header("Waste Reduction and Recycling")

    # User inputs
    plastic = st.number_input("Enter the amount of plastic waste generated (in kg)", min_value=0.0, value=0.0,step=0.1,format="%.1f",key="plastic")
    paper= st.number_input("Enter the amount of paper waste generated (in kg)", min_value=0.0, value=0.0,step=0.1,format="%.1f",key="paper")
    glass= st.number_input("Enter the amount of glass waste generated (in kg)", min_value=0.0, value=0.0,step=0.1,format="%.1f",key="glass")
    metal= st.number_input("Enter the amount of metal waste generated (in kg)", min_value=0.0, value=0.0,step=0.1,format="%.1f",key="metal")
    organic= st.number_input("Enter the amount of organic waste generated (in kg)", min_value=0.0, value=0.0,step=0.1,format="%.1f",key="organic")
    other= st.number_input("Enter the amount of other waste generated (in kg)", min_value=0.0, value=0.0,step=0.1,format="%.1f",key="other")
    recycled= st.number_input("Enter the amount of waste recycled (in kg)", min_value=0.0, value=0.0,step=0.1,format="%.1f",key="recycled")
    # Estimate waste reduction
    if st.button("Calculate"):
        total_waste = plastic+paper+glass+metal+organic+other
        if total_waste==0:
            recycled_percentage=0
        else:
            recycled_percentage = (recycled / total_waste) * 100
        st.write(f"\nTotal waste generated: {total_waste:.2f} kg")
        st.write(f"Percentage of waste recycled: {recycled_percentage:.2f}%")
        if recycled_percentage < 50:
            st.write("\nYour recycling rate is below 50%. Consider improving your recycling habits.")
        st.subheader("\n!!! Here are some tips to help you reduce waste:")
        st.write("Reduce: Avoid single-use products and choose reusable items.")
        st.write("Reuse: Find new uses for items instead of discarding them.")
        st.write("Recycle: Sort your waste properly to maximize recycling.")
        st.write("Compost: Compost organic waste to reduce landfill contributions.")
        st.write("Buy in bulk: Reduce packaging waste by buying in larger quantities.")
        st.write("Repair: Fix broken items instead of buying new ones.")
    button = st.button("Reset", on_click=reset_number_input_waste)

def main():
    st.title("Water Usage and Waste Reduction App")
    
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Choose a section", ["Water Usage Calculator", "Waste Reduction and Recycling"])
    
    if options == "Water Usage Calculator":
        water_usage_calculator()
    elif options == "Waste Reduction and Recycling":
        waste_reduction_and_recycling()

if __name__ == "__main__":
    main()