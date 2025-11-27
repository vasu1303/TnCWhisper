import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import { Cookie, Loader2, Sparkles } from "lucide-react";
import "../styles/tailwind.css";

// Mock summaries array - keyword-based
const MOCK_SUMMARIES: Record<string, string> = {
  "netflix": "- Payments are non-refundable and we do not provide refunds or credits for any partial membership periods or unused Netflix content\n- To cancel, go to the Account page and follow the instructions for cancellation\n- If you cancel your membership, your account will automatically close at the end of your current billing period\n- We may terminate or restrict your use of our service if you violate these Terms of Use or are engaged in illegal or fraudulent use of the service\n- The quality of the display of the Netflix content may vary from device to device\n- HD, Ultra HD and HDR availability is subject to your Internet service and device capabilities\n- Netflix does not accept unsolicited materials or ideas for Netflix content",
  
  "github": "- By using GitHub, you agree to comply with all applicable laws and regulations\n- You are responsible for all content posted and activity that occurs under your account\n- GitHub may suspend or terminate your access for violating terms of service\n- All user-generated content is licensed to GitHub for display and distribution\n- Private repositories remain private, but GitHub has access for technical support\n- Two-factor authentication is strongly recommended for security\n- API rate limits apply to prevent abuse of GitHub services\n- DMCA takedown notices are processed according to US copyright law\n- GitHub can modify terms with 30 days notice to users",
  
  "google": "- Google collects your search history, location data, and device information\n- Your data is used to personalize ads and improve Google services\n- You can delete your data from My Activity, but backups may persist\n- Google may share data with third parties for analytics and advertising\n- You grant Google a license to use content you upload to their services\n- Account security is your responsibility; enable 2FA for protection\n- Google reserves the right to suspend accounts for policy violations\n- Services are provided as-is without warranties\n- You agree to resolve disputes through binding arbitration",
  
  "facebook": "- Facebook collects data about you even if you don't have an account\n- Your data is shared with advertisers for targeted marketing\n- Content you post becomes licensed to Facebook for worldwide use\n- Facebook uses facial recognition and AI to analyze your photos\n- You can download your data, but deletion requests may take up to 90 days\n- Facebook is not responsible for third-party apps accessing your data\n- Messaging and calls may be monitored for safety and policy enforcement\n- Account deactivation is temporary; deletion is permanent\n- You must use your real name and identity on Facebook",
  
  "amazon": "- Amazon Prime membership auto-renews unless cancelled\n- Your purchase history is used for personalized recommendations\n- Amazon collects voice recordings from Alexa devices\n- Third-party sellers operate independently; Amazon is not liable for their products\n- Returns must be initiated within 30 days of delivery\n- Amazon reserves the right to refuse service or cancel orders\n- Your payment information is stored securely for future purchases\n- Amazon may share data with affiliates and partners\n- Promotional credits and gift cards are non-transferable",
  
  "twitter": "- Twitter owns a license to all content you tweet or post\n- Your tweets are public by default and can be viewed by anyone\n- Twitter uses your data for personalized ads and content recommendations\n- Account suspension can occur for violating community guidelines\n- Direct messages are not end-to-end encrypted\n- Twitter may share data with law enforcement when legally required\n- You are responsible for all activity on your account\n- Inactive accounts may be removed after prolonged inactivity\n- API access requires developer approval and compliance",
  
  "default": "- We collect your personal information including email, name, and browsing history\n- Your data may be shared with third-party advertisers\n- We use cookies to track your activity across websites\n- You can delete your account anytime, but data may be retained for up to 90 days\n- By using this service, you agree to arbitration for dispute resolution\n- We reserve the right to modify these terms with 30 days notice"
};

// Mock cookies array
const MOCK_COOKIES = [
  { domain: "example.com", expires: "2025-12-31", name: "session_id", sameSite: "Lax", secure: true, value: "abc123xyz789" },
  { domain: ".google.com", expires: "2026-06-15", name: "_ga", sameSite: "None", secure: true, value: "GA1.2.123456789.1234567890" },
  { domain: "example.com", expires: "Session", name: "user_pref", sameSite: "Strict", secure: false, value: "dark_mode=true" },
  { domain: ".facebook.com", expires: "2025-11-30", name: "fr", sameSite: "None", secure: true, value: "0ZvyVMNBkTJKABC.AWXyZ123.Aa.AAA" },
  { domain: "example.com", expires: "2026-01-15", name: "auth_token", sameSite: "Lax", secure: true, value: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" },
  { domain: ".youtube.com", expires: "2027-03-20", name: "CONSENT", sameSite: "None", secure: true, value: "PENDING+987" },
  { domain: "example.com", expires: "Session", name: "cart_items", sameSite: "Lax", secure: false, value: "item1,item2,item3" },
  { domain: ".twitter.com", expires: "2025-12-01", name: "guest_id", sameSite: "None", secure: true, value: "v1%3A167890123456789012" },
];

const Popup = () => {
  const [cookies, setCookies] = useState<typeof MOCK_COOKIES>([]);
  const [currentTab, setCurrentTab] = useState<chrome.tabs.Tab | undefined>();
  const [loading, setLoading] = useState(false);
  const [loadingCookies, setLoadingCookies] = useState(false);
  const [returnUrl, setReturnedUrl] = useState("");
  const [showCookies, setShowCookies] = useState(false);
  const [summary, setSummary] = useState("");
  const [tabUrl, setTabUrl] = useState<string | undefined>("");

  async function getCurrentTab() {
    let queryOptions = { active: true, lastFocusedWindow: true };
    let [tab] = await chrome.tabs.query(queryOptions);
    setCurrentTab(tab);
    if (tab) {
    setTabUrl(tab.url);
    }
  }

  const preProcess = async () => {
    if (!tabUrl) return;
    setLoading(true);
    setShowCookies(false);
    
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 1500 + Math.random() * 1000));
    
    try {
      // Extract domain/keyword from URL
      const urlObj = new URL(tabUrl);
      const hostname = urlObj.hostname.toLowerCase();
      
      // Find matching keyword
      let mockSummary = MOCK_SUMMARIES["default"];
      
      for (const keyword in MOCK_SUMMARIES) {
        if (hostname.includes(keyword)) {
          mockSummary = MOCK_SUMMARIES[keyword];
          break;
        }
      }
      
      setReturnedUrl(tabUrl);
      setSummary(mockSummary);
    } catch (error) {
      console.error("OOPS", error);
      setSummary(MOCK_SUMMARIES["default"]);
    }
    setLoading(false);
  };

  const fetchCookies = async () => {
    if (!tabUrl) return;
    setLoadingCookies(true);
    setSummary("");
    
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 2000 + Math.random() * 1500));
    
    try {
      // Extract domain from current tab URL
      const urlObj = new URL(tabUrl);
      const currentDomain = urlObj.hostname;
      
      // Mock: Use the predefined cookies with current domain
      const cookiesWithDomain = MOCK_COOKIES.map(cookie => ({
        ...cookie,
        domain: currentDomain
      }));
      
      setCookies(cookiesWithDomain);
      setShowCookies(true);
    } catch (error) {
      console.error("Error fetching cookies", error);
    }
    setLoadingCookies(false);
  };

  const bulletPoints = summary.split('\n').filter(line => line.trim().startsWith('-'));

  return (
    <div className="flex flex-col items-center w-[350px] h-[500px] bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 shadow-2xl rounded-xl border border-gray-700 p-4">
      {/* Header */}
      <div className="flex flex-col items-center w-full mb-2">
        <div className="flex items-center gap-2 mb-1">
          <Sparkles className="w-8 h-8 text-yellow-400 drop-shadow-lg" />
          <h1 className="text-2xl font-extrabold text-white tracking-tight drop-shadow-lg">
            TnC Summarizer
          </h1>
        </div>
        <span className="text-xs text-gray-400 font-medium tracking-wide">
          Powered by AI
        </span>
      </div>

      {/* Tab URL */}
      <button
        className="w-full border border-gray-600 bg-transparent text-white font-semibold py-2 rounded-lg shadow-sm hover:border-yellow-400 hover:text-yellow-400 transition mb-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        onClick={getCurrentTab}
      >
        Get Tab
      </button>
      {tabUrl && (
        <p className="text-xs text-blue-400 truncate w-full text-center mb-2">{tabUrl}</p>
      )}

      {/* Action Buttons */}
      <div className="w-full flex gap-2 mb-4">
        <button
          className="flex-1 border border-yellow-400 bg-yellow-400/10 text-yellow-300 font-bold py-2 rounded-lg shadow-sm hover:bg-yellow-400 hover:text-gray-900 transition focus:outline-none focus:ring-2 focus:ring-yellow-400"
          onClick={preProcess}
          disabled={loading || loadingCookies}
        >
          {loading ? (
            <span className="flex items-center justify-center gap-2">
              <Loader2 className="animate-spin h-4 w-4" />
              Summarizing...
            </span>
          ) : (
            "Summarize"
          )}
        </button>
        
        <button
          className="flex-1 border border-green-400 bg-green-400/10 text-green-300 font-bold py-2 rounded-lg shadow-sm hover:bg-green-400 hover:text-gray-900 transition focus:outline-none focus:ring-2 focus:ring-green-400 flex items-center justify-center gap-2"
          onClick={fetchCookies}
          disabled={loading || loadingCookies}
        >
          {loadingCookies ? (
            <>
              <Loader2 className="animate-spin h-4 w-4" />
              Loading...
            </>
          ) : (
            <>
              <Cookie className="h-4 w-4" />
              Cookies
            </>
          )}
        </button>
      </div>

      {/* Content Section */}
      <div className="flex-1 w-full bg-gray-800 bg-opacity-80 rounded-lg p-3 overflow-y-auto shadow-inner">
        {loading ? (
          <div className="flex flex-col items-center justify-center h-full">
            <Loader2 className="animate-spin h-6 w-6 text-yellow-400 mb-2" />
            <p className="text-yellow-300 font-semibold animate-pulse">Analyzing Terms &amp; Conditions...</p>
          </div>
        ) : loadingCookies ? (
          <div className="flex flex-col items-center justify-center h-full">
            <Loader2 className="animate-spin h-6 w-6 text-green-400 mb-2" />
            <p className="text-green-300 font-semibold animate-pulse">Fetching Cookies...</p>
          </div>
        ) : showCookies && cookies.length > 0 ? (
          <div className="space-y-3">
            <div className="flex items-center gap-2 mb-3">
              <Cookie className="h-5 w-5 text-green-400" />
              <h3 className="text-white font-bold text-sm">Website Cookies ({cookies.length})</h3>
            </div>
            {cookies.map((cookie, idx) => (
              <div key={idx} className="bg-gray-700 bg-opacity-50 rounded-lg p-3 border border-gray-600 hover:border-green-400 transition-all">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-green-300 font-semibold text-sm">{cookie.name}</span>
                  {cookie.secure && (
                    <span className="text-[10px] bg-blue-500 text-white px-2 py-0.5 rounded">Secure</span>
                  )}
                </div>
                <div className="space-y-1 text-xs text-gray-300">
                  <div className="flex justify-between">
                    <span className="text-gray-400">Domain:</span>
                    <span className="text-gray-200 truncate ml-2 max-w-[180px]">{cookie.domain}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-400">Expires:</span>
                    <span className="text-gray-200">{cookie.expires}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-400">SameSite:</span>
                    <span className="text-gray-200">{cookie.sameSite}</span>
                  </div>
                  <div className="mt-2">
                    <span className="text-gray-400">Value:</span>
                    <p className="text-gray-200 break-all mt-1 font-mono text-[10px] bg-gray-900 p-1 rounded">{cookie.value}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : bulletPoints.length > 0 ? (
          <ul className="list-disc list-inside text-gray-100 space-y-2 text-sm">
            {bulletPoints.map((point, idx) => (
              <li key={idx} className="transition-all duration-200 hover:text-yellow-400">{point.replace(/^- /, '')}</li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-400 text-center">No data yet. Click "Summarize" or "Cookies" to get started.</p>
        )}
      </div>

      {/* Footer */}
      <div className="w-full text-center mt-2">
        <span className="text-[10px] text-gray-500">© {new Date().getFullYear()} TnC Summarizer</span>
      </div>
    </div>
  );
};

export default Popup;

const container = document.getElementById("root");
const root = createRoot(container as HTMLDivElement);
root.render(<Popup />);
