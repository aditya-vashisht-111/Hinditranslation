import streamlit as st
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Hindi Vision Translator",
    page_icon="🕉️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = """
You are an expert Hindi-to-English Language Teacher and Note Designer.
When provided with an image of text, you must follow these rules strictly:

1. STRICT TRANSLATION FORMAT (Line-by-Line):
   - For every Hindi sentence or phrase, write the Hindi text first.
   - On the VERY NEXT LINE, write the full English translation.
   - Do NOT surround the English translation in parentheses. Just write the plain English text.
   - Example format:
     🔹 पेड़ के ऊपर बंदर बैठा है।
     A monkey is sitting on top of the tree.

2. BEAUTIFICATION (Design Mode):
   - Analyze the content structure and add relevant Emojis to Headers (e.g., 🌟, 📖, 💡, 🔹, ✅).
   - Use Bullet Points to organize lists.
   - Use **Bold** for keywords and grammatical terms.
   - The final output should look like a professional, aesthetic study guide.
   - Identify the main topic and create a decorative Main Title at the top.

If the image is blurry or illegible, politely ask for a clearer photo.
"""

# --- HELPER FUNCTIONS ---
def get_image_base64(uploaded_file):
    """Reads file buffer and returns base64 string."""
    try:
        bytes_data = uploaded_file.getvalue()
        return base64.b64encode(bytes_data).decode('utf-8')
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

def get_gemini_response(image_b64, mime_type):
    """Sends image and system prompt to Gemini 2.0 Flash."""
    
    # Initialize Model
    # Note: Ensure your langchain-google-genai library is up to date for 2.0 support
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=st.secrets["GOOGLE_API_KEY"],
        temperature=0.3, # Low temp for accurate translation
        max_output_tokens=4096
    )

    # Create the message payload
    # Gemini expects a list of content parts for multimodal input
    message = HumanMessage(
        content=[
            {"type": "text", "text": "Please analyze this Hindi textbook page and create the study notes."},
            {
                "type": "image_url", 
                "image_url": {"url": f"data:{mime_type};base64,{image_b64}"}
            }
        ]
    )

    # Invoke the chain
    try:
        response = llm.invoke([SystemMessage(content=SYSTEM_PROMPT), message])
        return response.content
    except Exception as e:
        return f"⚠️ Error connecting to Gemini: {str(e)}"

# --- UI LAYOUT ---

# Sidebar for inputs
with st.sidebar:
    st.header("📸 Upload Material")
    st.write("Upload a photo of your Hindi textbook.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    st.markdown("---")
    st.caption("Powered by Gemini 2.0 Flash & LangChain")

# Main Content Area
st.title("🇮🇳 Hindi Vision Translator")
st.markdown("Transform textbook photos into **beautiful, structured study notes** instantly.")

if uploaded_file:
    # Create a container for the output
    st.divider()
    
    # Generate Button
    if st.button("✨ Generate Study Notes", type="primary", use_container_width=True):
        
        with st.spinner("👀 Analyzing text and designing notes..."):
            # 1. Process Image
            image_b64 = get_image_base64(uploaded_file)
            mime_type = uploaded_file.type
            
            if image_b64:
                # 2. Get AI Response
                result_text = get_gemini_response(image_b64, mime_type)
                
                # 3. Display Result
                st.success("Translation Complete!")
                st.markdown(result_text)
                
                # 4. Download Button
                st.download_button(
                    label="📥 Download Notes as Text",
                    data=result_text,
                    file_name="Hindi_Study_Notes.md",
                    mime="text/markdown"
                )
else:
    # Empty State / Instructions
    st.info("👈 Please upload an image from the sidebar to get started.")
    
    # Example Preview
    with st.expander("See Example Output"):
        st.markdown("""
        ### 🌟 Lesson: The Jungle
        
        🔹 **शेर** जंगल का राजा है।
        The **lion** is the king of the jungle.
        
        🔹 वह बहुत **शक्तिशाली** होता है।
        He is very **powerful**.
        """)