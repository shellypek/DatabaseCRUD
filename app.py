import streamlit as st
import pandas as pd
import sqlalchemy as db

engine = db.create_engine(
    'postgresql://postgres:tiqcIg-5jixqe-quzzyw@db.amgskkqiswwpiytonjre.supabase.co:5432/postgres')
c = engine.connect()


def add_data_dt(id, description):
    query = "INSERT INTO public.disease_type VALUES ({}, '{}')".format(
        id, description)
    c.execute(query)


def add_data_c(cname, population):
    query = "INSERT INTO public.country VALUES ('{}', '{}')".format(
        cname, population)
    c.execute(query)


def add_data_disease(disease_code, pathogen, description, id):
    query = "INSERT INTO public.disease VALUES ('{}', '{}', '{}', {})".format(
        disease_code, pathogen, description, id)
    c.execute(query)


def add_data_discover(cname, disease_code, first_enc_date):
    query = "INSERT INTO public.discover VALUES ('{}', '{}', '{}')".format(
        cname, disease_code, first_enc_date)
    c.execute(query)


def add_data_users(email, name, surname, salary, phone, cname):
    query = "INSERT INTO public.users VALUES ('{}', '{}', '{}', {}, '{}', '{}')".format(
        email, name, surname, salary, phone, cname)
    c.execute(query)


def add_data_ps(email, department):
    query = "INSERT INTO public.public_servant VALUES ('{}', '{}')".format(
        email, department)
    c.execute(query)


def add_data_doctor(email, specialization):
    query = "INSERT INTO public.doctor VALUES ('{}', '{}')".format(
        email, specialization)
    c.execute(query)


def add_data_specialize(id, email):
    query = "INSERT INTO public.specialize VALUES ({}, '{}')".format(
        id, email)
    c.execute(query)


def add_data_record(email, cname, disease_code, total_deaths, total_patients):
    query = "INSERT INTO public.record VALUES ('{}', '{}', '{}', {}, {})".format(
        email, cname, disease_code, total_deaths, total_patients)
    c.execute(query)


def delete_data_dt(id):
    query = "DELETE FROM public.disease_type WHERE id = {}".format(id)
    c.execute(query)


def delete_data_c(cname):
    query = "DELETE FROM public.country WHERE cname = '{}'".format(cname)
    c.execute(query)


def delete_data_disease(disease_code):
    query = "DELETE FROM public.disease WHERE disease_code = '{}'".format(
        disease_code)
    c.execute(query)


def delete_data_discover(cname, disease_code):
    query = "DELETE FROM public.discover WHERE cname = '{}' AND disease_code = '{}'".format(
        cname, disease_code)
    c.execute(query)


def delete_data_users(email):
    query = "DELETE FROM public.users WHERE email = '{}'".format(email)
    c.execute(query)


def delete_data_ps(email):
    query = "DELETE FROM public.public_servant WHERE email = '{}'".format(
        email)
    c.execute(query)


def delete_data_doctor(email):
    query = "DELETE FROM public.doctor WHERE email = '{}'".format(email)
    c.execute(query)


def delete_data_specialize(id, email):
    query = "DELETE FROM public.specialize WHERE id = {} AND email = '{}'".format(
        id, email)
    c.execute(query)


def delete_data_record(email, cname, disease_code):
    query = "DELETE FROM public.record WHERE email = '{}' AND cname = '{}' AND disease_code = '{}'".format(
        email, cname, disease_code)
    c.execute(query)


def update_data_dt(id, description):
    query = "UPDATE public.disease_type SET description = '{}' WHERE id = {}".format(
        description, id)
    c.execute(query)


def update_data_c(cname, population):
    query = "UPDATE public.country SET population = '{}' WHERE cname = '{}'".format(
        population, cname)
    c.execute(query)


def update_data_disease(disease_code, pathogen, description, id):
    query = "UPDATE public.disease SET pathogen = '{}', description = '{}', id = {} WHERE disease_code = '{}'".format(
        pathogen, description, id, disease_code)
    c.execute(query)


def update_data_discover(cname, disease_code, first_enc_date):
    query = "UPDATE public.discover SET first_enc_date = '{}' WHERE cname = '{}' AND disease_code = '{}'".format(
        first_enc_date, cname, disease_code)
    c.execute(query)


def update_data_users(email, name, surname, salary, phone):
    query = "UPDATE public.users SET name = '{}', surname = '{}', salary = {}, phone = '{}' WHERE email = '{}'".format(
        name, surname, salary, phone, email)
    c.execute(query)


def update_data_ps(email, department):
    query = "UPDATE public.public_servant SET department = '{}' WHERE email = '{}'".format(
        department, email)
    c.execute(query)


def update_data_doctor(email, degree):
    query = "UPDATE public.doctor SET degree = '{}' WHERE email = '{}'".format(
        degree, email)
    c.execute(query)


def update_data_specialize(id, email):
    query = "UPDATE public.specialize SET id = {} WHERE email = '{}'".format(
        id, email)
    c.execute(query)


def update_data_record(email, cname, disease_code, total_deaths, total_patients):
    query = "UPDATE public.record SET total_deaths = {}, total_patients = {} WHERE email = '{}' AND cname = '{}' AND disease_code = '{}'".format(
        total_deaths, total_patients, email, cname, disease_code)
    c.execute(query)


def get_data(table_choice):
    dict = {
        "Disease Type": "disease_type",
        "Country": "country",
        "Disease": "disease",
        "Discover": "discover",
        "Users": "users",
        "Public Servant": "public_servant",
        "Doctor": "doctor",
        "Specialize": "specialize",
        "Record": "record"
    }
    query = "SELECT * FROM public.{}".format(dict[table_choice])
    res = c.execute(query)
    return res.fetchall()


def main():
    st.title("CRUD")
    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Create")
        tables = ["Disease Type", "Country", "Disease", "Discover",
                  "Users", "Public Servant", "Doctor", "Specialize", "Record"]
        table_choice = st.selectbox("Choose table", tables)

        if table_choice == "Disease Type":
            id = st.number_input("ID")
            id = int(id)
            description = st.text_area("Description")
            if st.button("Add Data"):
                add_data_dt(id, description)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Country":
            cname = st.text_input("Country Name")
            population = int(st.number_input("Population"))
            if st.button("Add Data"):
                add_data_c(cname, population)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Disease":
            disease_code = st.text_input("Disease Code")
            pathogen = st.text_input("Pathogen")
            description = st.text_area("Description")
            id = int(st.number_input("ID"))
            if st.button("Add Data"):
                add_data_disease(disease_code, pathogen, description, id)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Discover":
            cname = st.text_input("Country Name")
            disease_code = st.text_input("Disease Code")
            first_enc_date = st.date_input("First Encounter Date")
            if st.button("Add Data"):
                add_data_discover(cname, disease_code, first_enc_date)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Users":
            email = st.text_input("Email")
            name = st.text_input("Name")
            surname = st.text_input("Surname")
            salary = int(st.number_input("Salary"))
            phone = st.text_input("Phone")
            cname = st.text_input("Country Name")
            if st.button("Add Data"):
                add_data_users(email, name, surname, salary, phone, cname)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Public Servant":
            email = st.text_input("Email")
            department = st.text_input("Department")
            if st.button("Add Data"):
                add_data_ps(email, department)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Doctor":
            email = st.text_input("Email")
            degree = st.text_input("Degree")
            if st.button("Add Data"):
                add_data_doctor(email, degree)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Specialize":
            id = int(st.number_input("ID"))
            email = st.text_input("Email")
            if st.button("Add Data"):
                add_data_specialize(id, email)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        elif table_choice == "Record":
            email = st.text_input("Email")
            cname = st.text_input("Country Name")
            disease_code = st.text_input("Disease Code")
            total_deaths = int(st.number_input("Total Deaths"))
            total_patients = int(st.number_input("Total Patients"))
            if st.button("Add Data"):
                add_data_record(email, cname, disease_code,
                                total_deaths, total_patients)
                st.success("Added Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

    elif choice == "Read":
        st.subheader("Read")
        tables = ["Disease Type", "Country", "Disease", "Discover",
                  "Users", "Public Servant", "Doctor", "Specialize", "Record"]
        table_choice = st.selectbox("Table", tables)
        result = get_data(table_choice)
        st.write(pd.DataFrame(result))

    elif choice == "Update":
        st.subheader("Update")
        tables = ["Disease Type", "Country", "Disease", "Discover",
                  "Users", "Public Servant", "Doctor", "Specialize", "Record"]
        table_choice = st.selectbox("Table", tables)

        if table_choice == "Disease Type":
            id = st.number_input("Choose ID")
            id = int(id)
            description = st.text_area("Change description to")
            if st.button("Update Data"):
                update_data_dt(id, description)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Country":
            cname = st.text_input("Choose Country Name")
            population = int(st.number_input("Change population to"))
            if st.button("Update Data"):
                update_data_c(cname, population)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Disease":
            disease_code = st.text_input("Choose Disease Code")
            pathogen = st.text_input("Change pathogen to")
            description = st.text_area("Change description to")
            id = int(st.number_input("Change ID to"))
            if st.button("Update Data"):
                update_data_disease(disease_code, pathogen, description, id)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Discover":
            cname = st.text_input("Choose Country Name")
            disease_code = st.text_input("Choose Disease Code")
            first_enc_date = st.date_input("Change first encounter date to")
            if st.button("Update Data"):
                update_data_discover(cname, disease_code, first_enc_date)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Users":
            email = st.text_input("Choose Email")
            name = st.text_input("Change name to")
            surname = st.text_input("Change surname to")
            salary = int(st.number_input("Change salary to"))
            phone = st.text_input("Change phone to")
            cname = st.text_input("Change country name to")
            if st.button("Update Data"):
                update_data_users(email, name, surname, salary, phone, cname)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Public Servant":
            email = st.text_input("Choose Email")
            department = st.text_input("Change department to")
            if st.button("Update Data"):
                update_data_ps(email, department)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Doctor":
            email = st.text_input("Choose Email")
            degree = st.text_input("Change degree to")
            if st.button("Update Data"):
                update_data_doctor(email, degree)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Specialize":
            email = st.text_input("Choose Email")
            id = int(st.number_input("Change ID to"))
            if st.button("Update Data"):
                update_data_specialize(email, id)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Record":
            email = st.text_input("Choose Email")
            cname = st.text_input("Choose Country Name")
            disease_code = st.text_input("Choose Disease Code")
            total_deaths = int(st.number_input("Change total deaths to"))
            total_patients = int(st.number_input("Change total patients to"))
            if st.button("Update Data"):
                update_data_record(email, cname, disease_code,
                                   total_deaths, total_patients)
                st.success("Updated Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

    elif choice == "Delete":
        st.subheader("Delete")
        tables = ["Disease Type", "Country", "Disease", "Discover",
                  "Users", "Public Servant", "Doctor", "Specialize", "Record"]
        table_choice = st.selectbox("Table", tables)

        if table_choice == "Disease Type":
            id = st.number_input("ID")
            id = int(id)
            if st.button("Delete Data"):
                delete_data_dt(id)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Country":
            cname = st.text_input("Country Name")
            if st.button("Delete Data"):
                delete_data_c(cname)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Disease":
            disease_code = st.text_input("Disease Code")
            if st.button("Delete Data"):
                delete_data_disease(disease_code)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Discover":
            cname = st.text_input("Country Name")
            disease_code = st.text_input("Disease Code")
            if st.button("Delete Data"):
                delete_data_discover(cname, disease_code)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Users":
            email = st.text_input("Email")
            if st.button("Delete Data"):
                delete_data_users(email)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Public Servant":
            email = st.text_input("Email")
            if st.button("Delete Data"):
                delete_data_ps(email)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Doctor":
            email = st.text_input("Email")
            if st.button("Delete Data"):
                delete_data_doctor(email)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Specialize":
            id = st.number_input("ID")
            email = st.text_input("Email")
            if st.button("Delete Data"):
                delete_data_specialize(id, email)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))

        if table_choice == "Record":
            email = st.text_input("Email")
            cname = st.text_input("Country Name")
            disease_code = st.text_input("Disease Code")
            if st.button("Delete Data"):
                delete_data_record(email, cname, disease_code)
                st.success("Deleted Data")
            result = get_data(table_choice)
            st.write(pd.DataFrame(result))
    else:
        pass


if __name__ == '__main__':
    main()
