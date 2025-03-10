import streamlit as st
import re 

st.set_page_config(page_title="Password Strength Checker",page_icon="🔒")

st.title("🔐Possword Strength Checker ")
st.markdown("""
## welcome to the ultimate password Strength Checker!👋
            use  this simple tool to check the strength of your password and suggestions on how to make it strenger.
            we will  give you helpful tips to create a "Strong Password"🔓 """)

Password = st.text_input("Enter your password",type="password")

feedback = []

score = 0

if Password:
    if len(Password)  >= 8:
        score  += 1
    else :
        feedback.append("❌password should be at least 8 characters long.")

        if re.search(r'[A-Z]' , Password) and re.search (r'[A-Z]' , Password):
            score += 1
        else:
            feedback.append("❌Password should contain both upper and lower case  characters.")

            if re.search(r'\d', Password):
                score += 1 
            else :
                feedback.append("❌Password should contain at least one digit.")

                if re.search(r'[!@#$%&*]' , Password):
                    score  += 1
                else:
                    feedback.append("❌Password  should contain at least one special character (!@#$%&*).")
                    if score == 4:
                        feedback.append("✅ Your password is strong !🎉")
                    elif  score ==3:
                        feedback.append("🎯Your password is medium strength . It could be stronger.")
                    else:
                        feedback.append("👎Your password is weak . please make it stronger.")

                        if feedback:
                            st.markdown("## Improvment Suggestion")
                            for tip in feedback:
                                st.write(tip)
                            else:
                                st.info("please enter your password to get started.")