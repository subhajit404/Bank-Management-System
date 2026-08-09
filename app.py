import streamlit as st
from bank import Bank



# Page configuration


st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)



# Bank object


bank = Bank()



# Title


st.title("🏦 Bank Management System")
st.caption("Simple Banking Application using Python + Streamlit")

st.divider()



# Sidebar


st.sidebar.title("Bank Menu")

option = st.sidebar.radio(
    "Select an operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)



# CREATE ACCOUNT


if option == "Create Account":

    st.header("📝 Create New Account")

    name = st.text_input("Full Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )

    email = st.text_input("Email")

    pin = st.text_input(
        "4 Digit PIN",
        type="password",
        max_chars=4
    )

    if st.button("Create Account", type="primary"):

        if not name.strip():
            st.error("Please enter your name.")

        elif not email.strip():
            st.error("Please enter your email.")

        else:

            success, result = bank.create_account(
                name.strip(),
                age,
                email.strip(),
                pin
            )

            if success:

                st.success("Account created successfully!")

                st.info(
                    f"Your Account Number: **{result['accountNo']}**"
                )

                st.warning(
                    "Please save your account number safely."
                )

            else:
                st.error(result)



# DEPOSIT


elif option == "Deposit Money":

    st.header("💰 Deposit Money")

    account_no = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    amount = st.number_input(
        "Amount",
        min_value=0,
        max_value=10000,
        step=100
    )

    if st.button("Deposit Money", type="primary"):

        success, message = bank.deposit(
            account_no,
            pin,
            amount
        )

        if success:
            st.success(message)

        else:
            st.error(message)



# WITHDRAW


elif option == "Withdraw Money":

    st.header("💸 Withdraw Money")

    account_no = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    amount = st.number_input(
        "Amount",
        min_value=0,
        step=100
    )

    if st.button("Withdraw Money", type="primary"):

        success, message = bank.withdraw(
            account_no,
            pin,
            amount
        )

        if success:
            st.success(message)

        else:
            st.error(message)



# SHOW DETAILS


elif option == "Show Details":

    st.header("👤 Account Details")

    account_no = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    if st.button("Show Details", type="primary"):

        user = bank.get_details(
            account_no,
            pin
        )

        if user is None:

            st.error("Invalid account number or PIN.")

        else:

            st.success("Account found!")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Name**")
                st.write(user["name"])

                st.write("**Age**")
                st.write(user["age"])

                st.write("**Email**")
                st.write(user["email"])

            with col2:
                st.write("**Account Number**")
                st.write(user["accountNo"])

                st.write("**Balance**")
                st.metric(
                    "Current Balance",
                    f"₹{user['balance']}"
                )



# UPDATE DETAILS


elif option == "Update Details":

    st.header("✏️ Update Account")

    account_no = st.text_input("Account Number")

    pin = st.text_input(
        "Current PIN",
        type="password",
        max_chars=4
    )

    st.subheader("New Details")

    new_name = st.text_input(
        "New Name (leave empty to keep current)"
    )

    new_email = st.text_input(
        "New Email (leave empty to keep current)"
    )

    new_pin = st.text_input(
        "New PIN (leave empty to keep current)",
        type="password",
        max_chars=4
    )

    if st.button("Update Account", type="primary"):

        success, message = bank.update_account(
            account_no,
            pin,
            new_name.strip() or None,
            new_email.strip() or None,
            new_pin or None
        )

        if success:
            st.success(message)

        else:
            st.error(message)



# DELETE ACCOUNT


elif option == "Delete Account":

    st.header("🗑️ Delete Account")

    st.warning(
        "⚠️ Deleting your account is permanent."
    )

    account_no = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password",
        max_chars=4
    )

    confirm = st.checkbox(
        "I understand that this action cannot be undone."
    )

    if st.button(
        "Delete Account",
        type="primary"
    ):

        if not confirm:

            st.error(
                "Please confirm account deletion."
            )

        else:

            success, message = bank.delete_account(
                account_no,
                pin
            )

            if success:
                st.success(message)

            else:
                st.error(message)