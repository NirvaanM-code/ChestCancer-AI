import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="ChestCare AI", layout="wide")



st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(90deg, #cceeff, #e6e6ff);


    }
    </style>
    """,
    unsafe_allow_html=True
)



selected = option_menu(
    menu_title = None,
    options = ["Home", "Awareness", "Types of Chest Cancer", "Cancer Detection", "Contact Us"],
    icons = ["home","i","stethescope","Detect","Phone"],
    default_index = 0,
    orientation = "horizontal",
)

if selected == "Home":

    st.markdown(
        """
        <div style="text-align: center; margin-top: -15px; margin-bottom: 10px;">
            <h1 style="color: #007BFF;">ChestCare AI</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([1, 0.45, 1])
    with col1:
        st.write()
    with col2:
        st.image("logo5.png", width=200)

        

    # Main Banner
    st.markdown(
        """
        <div style="text-align: center; background-color: #f9f9f9; padding: 20px; margin-top: 15px; ">
            <h2 style="color: #007BFF;">Breathe Easy, Detect Early</h2>
            <p style="font-size: 18px;">Your partner in chest cancer awareness and detection</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.header("Why Early Detection Matters")
    st.write(
        "Early detection of chest cancer plays a crucial role in improving survival rates and treatment outcomes. When identified in its early stages, chest cancer is often localized, making it easier to treat with less invasive methods and a higher likelihood of success. Early detection can also help avoid the need for aggressive treatments like extensive chemotherapy or surgery, improving the patient’s quality of life. Additionally, recognizing symptoms early, such as persistent cough or chest pain, empowers individuals to take timely action. With advancements in technology like AI-powered diagnostics, detecting chest cancer early has become more accurate and accessible, offering patients and their families hope and a stronger chance for recovery. Early detection is not just about saving lives—it's about giving people the opportunity for better outcomes and peace of mind."
        )


    # Cards Section
    st.markdown(
    """
    <div style="display: flex; justify-content: space-around;">
        <div style="width: 30%; padding: 20px; margin-top: 20px; background-color: #e8f4ff; border-radius: 10px;">
            <h3 style="color: #007BFF;">Awareness</h3>
            <p>Understand the risks and signs of chest cancer. Knowledge is your first line of defense.</p>
        </div>
        <div style="width: 30%; padding: 20px;  margin-top: 20px; background-color: #ffe8f0; border-radius: 10px;">
            <h3 style="color: #FF69B4;">Types of Chest Cancer</h3>
            <p>Learn about the different types of chest cancer to stay informed.</p>
        </div>
        <div style="width: 30%; padding: 20px;  margin-top: 20px; background-color: #e8ffe8; border-radius: 10px;">
            <h3 style="color: #20C997;">AI Detection</h3>
            <p>Our AI-powered tool provides accurate and early detection results.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
        )

if selected == "Awareness":
    st.title("Chest Cancer Awareness")
    st.write("Chest cancer is one of the most pressing health challenges worldwide, impacting millions of individuals each year. Raising awareness about chest cancer is crucial to empowering communities with the knowledge and tools needed to take effective preventive measures. It also ensures that those affected receive the support they need while working to reduce the stigma that often surrounds the disease. By fostering a deeper understanding of chest cancer, we can promote early detection, encourage timely medical interventions, and build a strong collective effort to combat this life-threatening condition. Awareness serves as a bridge to better healthcare, stronger support networks, and ultimately, improved outcomes for individuals and families impacted by chest cancer.")
    st.write("")
    col1, col2, col3 = st.columns([1,1,1.2])
    with col1:
        st.image("1n.jpg", width = 400)
    with col2:
        st.image("2n.jpeg", width = 374)
    with col3:
        st.image("3n.jpg", width = 500)
    st.title("Key Facts about Chest Cancer")
    st.markdown(
    """
    <div style="display: flex; justify-content: space-around;">
        <div style="width: 48%; padding: 20px; margin-top: 20px; background-color: #e8f4ff; border-radius: 10px;">
            <h3 style="color: #007BFF;">Chest cancer encompasses various forms of cancer that develop in the chest region, including lung cancer and cancers of the chest wall or mediastinum.</h3>
            <p></p>
        </div>
        <div style="width: 48%; padding: 20px;  margin-top: 20px; background-color: #e8ffe8; border-radius: 10px;">
            <h3 style="color: #29a329">It affects people of all ages, genders, and backgrounds, although certain factors like smoking, environmental pollution, and occupational hazards can increase the risk.</h3>
            <p></p>
        </div>
        

    </div>
    """,
    unsafe_allow_html=True
        )
    st.title("Preventive Measures")
    st.write("")
    
    col1, col2, col3, col4 = st.columns([1, 0.45, 0.95, 0.5])
    with col1:
        st.write("**Avoid Tobacco:**")
        st.write("Smoking is the leading cause of lung cancer and other chest-related cancers. Quitting smoking or avoiding exposure to secondhand smoke is one of the most effective ways to reduce the risk.")
 

    with col2:
        st.image("cig.png", width = 150)
   
    with col3:
        st.write("**Maintain a Healthy Diet:**")
        st.write("A balanced diet rich in fruits, vegetables, whole grains, and lean proteins strengthens the immune system and provides essential nutrients that help fight cellular damage.")

    with col4:
        st.image("hd.png", width =150)

    st.write("")
    
       
    col1, col2, col3, col4 = st.columns([0.45, 1, 0.4, 1.2])
    
    with col1:
        st.image("dumb.png", width = 150)

    with col2:

        st.write("**Regular Exercise:**")
        st.write("Physical activity helps maintain a healthy weight and reduces inflammation, both of which are linked to lower cancer risks.")

    with col3:
        st.image("Skull.jpg", width = 150)
    with col4:
        st.write("**Minimize Exposure to Environmental Toxins:**")
        st.write("Limit exposure to harmful pollutants, such as asbestos, radon gas, and industrial fumes, which are known carcinogens.")
    
if selected == "Types of Chest Cancer":
    st.title("Types of Chest Cancer")
    st.write("Chest cancer encompasses a variety of cancers that originate in the chest region, including the lungs, breast tissue, esophagus, thymus, and chest wall. Each type of chest cancer presents unique challenges, symptoms, and treatment options. Understanding the different types of chest cancer is crucial for raising awareness, promoting early detection, and improving outcomes for those affected. This section provides a comprehensive overview of the most common types of chest cancer, their key characteristics, and their impact on individuals and communities. By learning about these cancers, we can take steps toward prevention, timely diagnosis, and effective care.")
    col1, col2, col3 = st.columns([1,1,0.95])
    with col1:
        st.title("Lung Cancer")
        st.image("Lung.png", width = 500)
        st.write("Lung cancer is one of the most prevalent and serious types of chest cancer. It originates in the lungs and is primarily categorized into two types: Non-Small Cell Lung Cancer (NSCLC) and Small Cell Lung Cancer (SCLC). NSCLC accounts for the majority of cases and includes subtypes like adenocarcinoma, squamous cell carcinoma, and large cell carcinoma. SCLC, on the other hand, is more aggressive and spreads quickly. Common symptoms include a persistent cough, shortness of breath, chest pain, and unexplained weight loss. Smoking is the leading cause of lung cancer, but exposure to environmental toxins like radon gas and asbestos also increases the risk.")
       
        st.title("Esophogeal Cancer")
        st.image("Esophag.png", width = 500)
        st.write("Esophageal cancer affects the esophagus, which connects the throat to the stomach. It often impacts the chest region as the cancer progresses. Adenocarcinoma, common in the lower esophagus, and Squamous Cell Carcinoma, prevalent in the upper and middle esophagus, are the two primary types. Symptoms include difficulty swallowing, chest discomfort, weight loss, and hoarseness. Risk factors include chronic acid reflux, smoking, and heavy alcohol consumption.")
    with col2:
        st.title("Breast Cancer")
        st.image("Breast.png", width = 500)
        st.write("Although primarily associated with women, breast cancer can also affect men. It develops from abnormal growth in the breast tissue and can spread to nearby areas, including the chest wall. The most common types include Invasive Ductal Carcinoma (IDC) and Invasive Lobular Carcinoma (ILC). Symptoms often include lumps in the breast or underarm, changes in breast size or shape, nipple discharge, or skin dimpling. Hormonal factors, genetic mutations (e.g., BRCA1/BRCA2), and a family history of breast cancer are significant risk factors.")
        st.write("")
        st.write("")
        st.write("")
        st.title("Mesothelioma")
        st.image("Meso.png", width = 500)
        st.write("Pleural mesothelioma is a rare cancer affecting the pleura, the thin layer of tissue surrounding the lungs. It is strongly associated with asbestos exposure. Symptoms include persistent chest pain, difficulty breathing, and fluid accumulation around the lungs. Occupational hazards and prolonged exposure to asbestos are the main causes. Early treatment can help manage symptoms and improve quality of life.")
    with col3:
        st.title("Thymoma & Thymic Carcinoma")
        st.image("Thymoma.png")
        st.write("Thymoma and thymic carcinoma are rare cancers originating in the thymus, a small organ in the chest. Thymoma is typically slow-growing and often linked to autoimmune diseases like myasthenia gravis. Thymic carcinoma is more aggressive and spreads rapidly. Symptoms may include persistent cough, chest pain, and difficulty breathing. Early diagnosis is key to managing these cancers effectively.")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("Chest Wall Tumors")
        st.image("Chestwall.png", width = 500)
        st.write("Chest wall tumors develop in the bones, muscles, or soft tissues of the chest. They can be primary (originating in the chest wall) or secondary (metastatic). While many primary tumors are benign, secondary tumors are often malignant. Symptoms include localized pain, swelling, and restricted movement. Early medical evaluation is critical for appropriate treatment.")
if selected == "Cancer Detection":
    st.title("AI Detection")
    st.write("Utilize our AI-powered detection tools for early diagnosis.")
    
    @st.cache_resource
    def models():
        mod = YOLO("best.pt")
        return mod

    img = st.file_uploader("Upload your image", type = ["jpg", "png", "jpeg"])
    analyse = st.button("Analyse/Submit")

    if analyse:
        if img != None:
            img = Image.open(img)
            st.markdown("Image Visualisation")
            st.image(img)
            st.subheader("Detected Cancer: ")
            model = models()
            res = model.predict(img)
            top_label = res[0].probs.top5[0]  
            class_name = res[0].names[top_label]  
            confidence = res[0].probs.top5conf[0]  
            if class_name == "squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa":
                st.write("Detected Cancer: Squamous Cell Carcinoma")
                st.write(f"Confidence Level: {confidence:.2f}")

            elif class_name == "adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib":
                st.write("Detected Cancer: Adenocarcinoma")
                st.write(f"Confidence Level: {confidence:.2f}")

            elif class_name == "large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa":
                st.write("Detected Cancer: Large Cell Carcinoma")
                st.write(f"Confidence Level: {confidence:.2f}")

            elif class_name == "normal":
                st.write("Detected Cancer: Normal - No Cancer Detected")
                st.write(f"Confidence Level: {confidence:.2f}")

if selected == "Contact Us":
    st.title("Contact Us")
    st.write("If you have questions, need assistance, or want to collaborate with us, we’re here to help. Feel free to reach out using the options below, and we’ll get back to you as soon as possible.")
    st.title("Email Adress:")
    st.write("info@chestcareai.com")
    st.title("Phone Number:")
    st.write("+91 9990906347")
    st.title("Address")
    st.write("123 ChestCare Lane,")
    st.write("Connaught Place,")
    st.write("New Delhi, 110001,")
    st.write("Delhi, India")

    st.title("General Queries")
    st.write("**1. What is Chest Cancer?**")
    st.write("Chest cancer is a term used to describe various types of cancers that originate in the chest region, including the lungs, breast tissue, esophagus, thymus, and chest wall. Each type has distinct characteristics, causes, and symptoms. These cancers can affect individuals of all genders and ages and may require different approaches for diagnosis and treatment depending on their location and stage.")
    st.write("**2. What are the symptoms of chest cancer?**")
    st.write("The symptoms of chest cancer vary depending on the specific type, but common indicators include a persistent cough, chest pain, shortness of breath, and unexplained weight loss. In some cases, individuals may also notice lumps or swelling in the chest area. It is important to pay attention to these symptoms and consult a healthcare professional promptly, as early detection can significantly improve treatment outcomes.")
    st.write("**3. Who is at risk of developing chest cancer?**")
    st.write("Certain factors increase the risk of developing chest cancer, including smoking, exposure to secondhand smoke, and long-term contact with environmental toxins such as asbestos or radon gas. A family history of cancer, genetic mutations, and chronic acid reflux (in the case of esophageal cancer) can also contribute to a higher risk. While these factors do not guarantee the development of chest cancer, they highlight the importance of awareness and preventive measures.")
    st.write("**4. How can chest cancer be detected?**")
    st.write("Chest cancer is detected through a variety of diagnostic tools depending on the type of cancer. Imaging tests like X-rays, CT scans, and MRIs are commonly used to visualize abnormalities in the chest. In some cases, a biopsy is performed to examine a tissue sample for cancerous cells. For specific cancers, such as breast cancer or lung cancer, tools like mammograms and low-dose CT scans are used. Early detection through regular screenings can save lives by catching the disease before it progresses.")
    st.write("**5. Is chest cancer preventable?**")
    st.write("While not all cases of chest cancer can be prevented, several steps can significantly reduce the risk. Avoiding tobacco use and minimizing exposure to carcinogens like asbestos or radon gas are critical measures. Maintaining a healthy lifestyle with a balanced diet and regular exercise also helps reduce the overall risk. Additionally, routine screenings for high-risk individuals play an important role in identifying potential issues early and preventing complications.")



